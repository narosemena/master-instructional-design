#!/usr/bin/env python3
"""
Generate a populated document from a user template using a confirmed field mapping.

Usage:
  # Generate (uses saved mapping from templates/mappings.json if available):
  python3 generate_doc.py --type TYPE --template PATH --data JSON [--out PATH]

  # Save a confirmed mapping without generating:
  python3 generate_doc.py --save-mapping --template PATH --mapping JSON

  # Generate with inline mapping and save it for future sessions:
  python3 generate_doc.py --type TYPE --template PATH --data JSON \
    --mapping JSON --save-mapping [--out PATH]

Supported types and output formats:
  storyboard        → .pptx
  facilitator-guide → .docx
  alignment-matrix  → .xlsx

─────────────────────────────────────────────────────────────────────────────
DATA SCHEMAS
─────────────────────────────────────────────────────────────────────────────

storyboard:
  {
    "title": "Course — Module 1",
    "version": "v1.0",
    "date": "YYYY-MM-DD",
    "slides": [
      {
        "num": 1,
        "type": "Title | Content | Scenario | Knowledge Check",
        "text": "On-screen text",
        "narration": "Narration script (always placed in slide notes)",
        "visual": "Visual description for developer",
        "interaction": "None | Click to reveal | Branch choice | MCQ",
        "dev_notes": "Developer production notes"
      }
    ]
  }

facilitator-guide:
  {
    "title": "Workshop Name",
    "length": "4 hrs",
    "max_participants": 20,
    "format": "ILT | VILT",
    "materials": ["Slide deck", "Handout A"],
    "setup": "Room / platform setup notes",
    "activities": [
      {
        "time": "0:00",
        "activity": "Opening",
        "action": "Facilitator action description",
        "responses": "Anticipated participant responses",
        "notes": "Internal notes"
      }
    ],
    "debrief": ["Question 1", "Question 2"],
    "troubleshooting": [
      {"situation": "Group disengages", "response": "Break into pairs"}
    ]
  }

alignment-matrix:
  {
    "title": "Module Alignment Matrix",
    "rows": [
      {
        "objective": "Full objective text",
        "bloom": "Remember | Understand | Apply | Analyze | Evaluate | Create",
        "strategy": "Instructional strategy",
        "assessment": "Assessment method",
        "media": "Media type",
        "duration": "X min"
      }
    ]
  }

─────────────────────────────────────────────────────────────────────────────
MAPPING SCHEMAS  (stored in templates/mappings.json, keyed by template basename)
─────────────────────────────────────────────────────────────────────────────

storyboard (.pptx):
  {
    "slide_types": {
      "Title": "Title Slide",          ← layout name in the template
      "Content": "Two Content",
      "Scenario": "Two Content",
      "Knowledge Check": "Blank"
    },
    "fields": {
      "0": "text",                     ← placeholder idx → data field
      "1": "visual"
    }
  }
  Note: narration always goes to slide notes regardless of mapping.
  Note: visual/interaction/dev_notes not in fields map are appended to notes.

facilitator-guide (.docx):
  {
    "session_plan_table": 0,           ← 0-based table index for session plan
    "column_map": {
      "time": "Time",                  ← data field → column header in template
      "activity": "Activity",
      "action": "Facilitator Action",
      "responses": "Anticipated Responses",
      "notes": "Notes"
    },
    "troubleshooting_table": 1         ← optional: 0-based index of troubleshooting table
  }

alignment-matrix (.xlsx):
  {
    "column_map": {
      "objective": "Learning Objective",   ← data field → column header in template
      "bloom": "Bloom's Level",
      "strategy": "Instructional Strategy",
      "assessment": "Assessment Method",
      "media": "Media Type",
      "duration": "Duration"
    }
  }
"""
import argparse
import json
import os
import sys
from datetime import date


MAPPINGS_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "templates",
    "mappings.json",
)

TYPE_EXT = {
    "storyboard": "pptx",
    "facilitator-guide": "docx",
    "alignment-matrix": "xlsx",
}

BLOOM_COLORS = {
    "Remember": "DBEAFE",
    "Understand": "BBF7D0",
    "Apply": "FEF08A",
    "Analyze": "FED7AA",
    "Evaluate": "FECACA",
    "Create": "E9D5FF",
}


# ─── Mapping persistence ──────────────────────────────────────────────────────

def load_mappings():
    if os.path.exists(MAPPINGS_PATH):
        with open(MAPPINGS_PATH) as f:
            return json.load(f)
    return {}


def save_mapping(template_basename, mapping):
    mappings = load_mappings()
    mappings[template_basename] = mapping
    os.makedirs(os.path.dirname(MAPPINGS_PATH), exist_ok=True)
    with open(MAPPINGS_PATH, "w") as f:
        json.dump(mappings, f, indent=2)
    print(json.dumps({"saved": template_basename, "path": MAPPINGS_PATH}))


def resolve_mapping(template_path, mapping_arg):
    """Return (mapping_dict, source_description)."""
    if mapping_arg:
        # Inline JSON or path to JSON file
        if mapping_arg.strip().startswith("{"):
            return json.loads(mapping_arg), "inline"
        with open(mapping_arg) as f:
            return json.load(f), mapping_arg

    basename = os.path.basename(template_path)
    mappings = load_mappings()
    if basename in mappings:
        return mappings[basename], f"templates/mappings.json ({basename})"

    return None, None


# ─── XLSX generator ───────────────────────────────────────────────────────────

def generate_xlsx(template_path, data, mapping, output_path):
    from openpyxl import load_workbook
    from openpyxl.styles import PatternFill

    wb = load_workbook(template_path)
    ws = wb.active

    column_map = mapping.get("column_map", {})
    fields = ["objective", "bloom", "strategy", "assessment", "media", "duration"]

    # Find header row (first non-empty row within first 10)
    header_row_idx = 1
    for i, row in enumerate(ws.iter_rows(min_row=1, max_row=10, values_only=True), start=1):
        if any(v for v in row):
            header_row_idx = i
            break

    # Map field names → column indices using column_map
    header_cells = list(ws.iter_rows(
        min_row=header_row_idx, max_row=header_row_idx
    ))[0]
    header_to_col = {
        cell.value: cell.column
        for cell in header_cells
        if cell.value is not None
    }

    col_indices = {}
    for field in fields:
        col_header = column_map.get(field)
        if col_header and col_header in header_to_col:
            col_indices[field] = header_to_col[col_header]

    # Write data rows
    start_row = header_row_idx + 1
    for i, row_data in enumerate(data.get("rows", [])):
        for field, col_idx in col_indices.items():
            cell = ws.cell(row=start_row + i, column=col_idx)
            cell.value = row_data.get(field, "")
            if field == "bloom":
                color = BLOOM_COLORS.get(row_data.get("bloom", ""))
                if color:
                    cell.fill = PatternFill(
                        start_color=color, end_color=color, fill_type="solid"
                    )

    wb.save(output_path)


# ─── DOCX generator ───────────────────────────────────────────────────────────

def generate_docx(template_path, data, mapping, output_path):
    from docx import Document
    from docx.shared import Pt
    from docx.oxml.ns import qn
    import copy

    doc = Document(template_path)

    column_map = mapping.get("column_map", {
        "time": "Time",
        "activity": "Activity",
        "action": "Facilitator Action",
        "responses": "Anticipated Responses",
        "notes": "Notes",
    })
    session_plan_idx = mapping.get("session_plan_table", 0)
    troubleshooting_idx = mapping.get("troubleshooting_table", None)

    # Replace title placeholder in the first Title/Heading 1 paragraph
    for para in doc.paragraphs:
        if para.style.name in ("Title", "Heading 1") and para.text.strip():
            for run in para.runs:
                run.text = ""
            if para.runs:
                para.runs[0].text = data.get("title", "Facilitator Guide")
            break

    # Populate session plan table
    if doc.tables and session_plan_idx < len(doc.tables):
        tbl = doc.tables[session_plan_idx]

        # Build column index map from table header row
        if tbl.rows:
            header_cells = tbl.rows[0].cells
            col_by_header = {
                cell.text.strip(): i for i, cell in enumerate(header_cells)
            }

        act_fields = ["time", "activity", "action", "responses", "notes"]
        col_order = [
            col_by_header.get(column_map.get(f, ""), -1) for f in act_fields
        ]

        # Remove existing data rows (keep header)
        for row in tbl.rows[1:]:
            tbl._tbl.remove(row._tr)

        # Add activity rows
        for activity in data.get("activities", []):
            row = tbl.add_row()
            for field, col_idx in zip(act_fields, col_order):
                if 0 <= col_idx < len(row.cells):
                    row.cells[col_idx].text = str(activity.get(field, ""))

    # Populate troubleshooting table if mapped
    if troubleshooting_idx is not None and doc.tables and troubleshooting_idx < len(doc.tables):
        tbl = doc.tables[troubleshooting_idx]
        for row in tbl.rows[1:]:
            tbl._tbl.remove(row._tr)
        for item in data.get("troubleshooting", []):
            row = tbl.add_row()
            if len(row.cells) >= 2:
                row.cells[0].text = item.get("situation", "")
                row.cells[1].text = item.get("response", "")

    doc.save(output_path)


# ─── PPTX generator ───────────────────────────────────────────────────────────

def generate_pptx(template_path, data, mapping, output_path):
    from pptx import Presentation

    prs = Presentation(template_path)

    slide_types = mapping.get("slide_types", {})
    fields_map = mapping.get("fields", {})  # {placeholder_idx_str: data_field}

    layout_by_name = {layout.name: layout for layout in prs.slide_layouts}
    default_layout = prs.slide_layouts[min(1, len(prs.slide_layouts) - 1)]

    for slide_data in data.get("slides", []):
        slide_type = slide_data.get("type", "Content")
        layout_name = slide_types.get(slide_type)
        layout = layout_by_name.get(layout_name, default_layout)

        slide = prs.slides.add_slide(layout)

        # Populate placeholders per mapping
        for ph in slide.placeholders:
            idx_str = str(ph.placeholder_format.idx)
            field = fields_map.get(idx_str)
            if field and slide_data.get(field):
                try:
                    ph.text = str(slide_data[field])
                except Exception:
                    pass  # Read-only or locked placeholder

        # Narration always goes to slide notes (PowerPoint convention)
        narration = slide_data.get("narration", "")
        extra = "\n".join(filter(None, [
            slide_data.get("visual", ""),
            f"Interaction: {slide_data.get('interaction', '')}" if slide_data.get("interaction") else "",
            f"Dev notes: {slide_data.get('dev_notes', '')}" if slide_data.get("dev_notes") else "",
        ]))
        notes_text = "\n\n".join(filter(None, [narration, extra]))
        if notes_text:
            slide.notes_slide.notes_text_frame.text = notes_text

    prs.save(output_path)


# ─── Output path helper ───────────────────────────────────────────────────────

def build_output_path(doc_type, title, template_path):
    ext = TYPE_EXT.get(doc_type, "")
    slug = title.lower().replace(" ", "-").replace("—", "").replace("/", "-")
    slug = "".join(c for c in slug if c.isalnum() or c == "-").strip("-")[:60]
    out_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "generated",
    )
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, f"{slug}.{ext}")


# ─── Entry point ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Populate a user template with structured L&D content"
    )
    parser.add_argument("--type", choices=list(TYPE_EXT.keys()))
    parser.add_argument("--template", required=True, help="Path to template file")
    parser.add_argument("--data", help="JSON string of document content")
    parser.add_argument("--mapping", help="JSON string or path to mapping file")
    parser.add_argument("--save-mapping", action="store_true",
                        help="Persist --mapping to templates/mappings.json")
    parser.add_argument("--out", help="Output file path (default: generated/<slug>.<ext>)")
    args = parser.parse_args()

    if not os.path.exists(args.template):
        print(json.dumps({"error": f"Template not found: {args.template}"}))
        sys.exit(1)

    # Save-mapping-only mode
    if args.save_mapping and not args.data:
        if not args.mapping:
            print(json.dumps({"error": "--mapping required with --save-mapping"}))
            sys.exit(1)
        mapping = json.loads(args.mapping) if args.mapping.strip().startswith("{") \
            else json.load(open(args.mapping))
        save_mapping(os.path.basename(args.template), mapping)
        return

    if not args.type:
        print(json.dumps({"error": "--type required for generation"}))
        sys.exit(1)

    if not args.data:
        print(json.dumps({"error": "--data required for generation"}))
        sys.exit(1)

    # Resolve mapping
    mapping, mapping_source = resolve_mapping(args.template, args.mapping)
    if mapping is None:
        print(json.dumps({
            "error": "no_mapping",
            "message": (
                f"No mapping found for '{os.path.basename(args.template)}'. "
                "Run analyze_template.py to inspect the template structure, "
                "confirm field equivalencies, then pass --mapping JSON --save-mapping."
            )
        }))
        sys.exit(2)  # Exit 2 = mapping needed (not a crash)

    # Save mapping if requested
    if args.save_mapping and args.mapping:
        save_mapping(os.path.basename(args.template), mapping)

    data = json.loads(args.data)
    title = data.get("title", args.type)
    output_path = args.out or build_output_path(args.type, title, args.template)

    try:
        if args.type == "storyboard":
            generate_pptx(args.template, data, mapping, output_path)
        elif args.type == "facilitator-guide":
            generate_docx(args.template, data, mapping, output_path)
        elif args.type == "alignment-matrix":
            generate_xlsx(args.template, data, mapping, output_path)

        print(json.dumps({
            "output": output_path,
            "type": args.type,
            "mapping_source": mapping_source,
            "slides_or_rows": (
                len(data.get("slides", data.get("rows", data.get("activities", []))))
            ),
        }))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)


if __name__ == "__main__":
    main()

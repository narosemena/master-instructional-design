#!/usr/bin/env python3
"""
Analyze a template file and output its structure as JSON.

Usage:
  python3 analyze_template.py --file PATH

Output (stdout): JSON describing the template's structural elements.

  .pptx  — slide layouts (name, placeholder idx/name/type), existing slide count
            and per-slide layout + text preview
  .docx  — paragraph styles used, heading hierarchy, table headers and dimensions
  .xlsx  — sheet names, header row values, row count per sheet

The output is intended to be read by Claude to surface mapping questions
before any population is attempted.
"""
import argparse
import json
import os
import sys


def analyze_pptx(path):
    from pptx import Presentation

    prs = Presentation(path)

    layouts = []
    for layout in prs.slide_layouts:
        placeholders = []
        for ph in layout.placeholders:
            placeholders.append({
                "idx": ph.placeholder_format.idx,
                "name": ph.name,
                "type": str(ph.placeholder_format.type).split(".")[-1],
            })
        layouts.append({"name": layout.name, "placeholders": placeholders})

    existing_slides = []
    for i, slide in enumerate(prs.slides):
        frames = []
        for shape in slide.shapes:
            if shape.has_text_frame:
                text = shape.text_frame.text.strip()
                if text:
                    frames.append({"shape": shape.name, "preview": text[:80]})
        existing_slides.append({
            "num": i + 1,
            "layout": slide.slide_layout.name,
            "text_frames": frames,
        })

    return {
        "type": "pptx",
        "existing_slide_count": len(prs.slides),
        "existing_slides": existing_slides,
        "layouts": layouts,
    }


def analyze_docx(path):
    from docx import Document

    doc = Document(path)

    styles_used = sorted({p.style.name for p in doc.paragraphs if p.text.strip()})
    headings = [
        {"style": p.style.name, "text": p.text}
        for p in doc.paragraphs
        if p.style.name.startswith("Heading") and p.text.strip()
    ]

    tables = []
    for i, tbl in enumerate(doc.tables):
        headers = [c.text.strip() for c in tbl.rows[0].cells] if tbl.rows else []
        tables.append({
            "table_num": i + 1,
            "headers": headers,
            "row_count": len(tbl.rows),
            "col_count": len(tbl.columns),
        })

    return {
        "type": "docx",
        "styles_used": styles_used,
        "headings": headings,
        "tables": tables,
    }


def analyze_xlsx(path):
    from openpyxl import load_workbook

    wb = load_workbook(path, read_only=True)
    sheets = []
    for name in wb.sheetnames:
        ws = wb[name]
        headers = []
        for row in ws.iter_rows(min_row=1, max_row=1, values_only=True):
            headers = [str(h) if h is not None else "" for h in row]
        sheets.append({
            "name": name,
            "headers": headers,
            "row_count": ws.max_row or 0,
        })
    wb.close()
    return {"type": "xlsx", "sheets": sheets}


def main():
    parser = argparse.ArgumentParser(
        description="Analyze a template file and output its structure as JSON"
    )
    parser.add_argument("--file", required=True, help="Path to template file")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(json.dumps({"error": f"File not found: {args.file}"}))
        sys.exit(1)

    ext = os.path.splitext(args.file)[1].lower()
    try:
        if ext == ".pptx":
            result = analyze_pptx(args.file)
        elif ext in (".docx", ".doc"):
            result = analyze_docx(args.file)
        elif ext in (".xlsx", ".xls"):
            result = analyze_xlsx(args.file)
        else:
            print(json.dumps({"error": f"Unsupported file type: {ext}"}))
            sys.exit(1)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)


if __name__ == "__main__":
    main()

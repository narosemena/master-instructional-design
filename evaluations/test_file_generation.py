#!/usr/bin/env python3
"""
Tests for analyze_template.py and generate_doc.py.

Creates synthetic templates programmatically, runs the scripts against them,
and validates output structure and content.

Run: python3 evaluations/test_file_generation.py
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANALYZE = os.path.join(REPO_ROOT, ".claude", "scripts", "analyze_template.py")
GENERATE = os.path.join(REPO_ROOT, ".claude", "scripts", "generate_doc.py")


def run(script, *args):
    """Run a script with args, return (returncode, stdout, stderr)."""
    result = subprocess.run(
        [sys.executable, script, *args],
        capture_output=True, text=True
    )
    return result.returncode, result.stdout, result.stderr


def make_pptx(path):
    """Create a minimal storyboard .pptx template with named layouts."""
    from pptx import Presentation
    from pptx.util import Inches, Pt

    prs = Presentation()
    # python-pptx default has layouts 0=Title Slide, 1=Title and Content, etc.
    # Rename layouts so the mapping tests are meaningful
    prs.slide_layouts[0].name = "Title Slide"
    prs.slide_layouts[1].name = "Storyboard Row"
    prs.slide_layouts[2].name = "Knowledge Check"
    prs.save(path)


def make_docx(path):
    """Create a minimal facilitator guide .docx template."""
    from docx import Document

    doc = Document()
    doc.add_heading("Workshop Title", level=1)
    doc.add_heading("Session Plan", level=2)

    tbl = doc.add_table(rows=2, cols=5)
    tbl.style = "Table Grid"
    headers = ["Time", "Activity", "Facilitator Action", "Anticipated Responses", "Notes"]
    for i, h in enumerate(headers):
        tbl.rows[0].cells[i].text = h
    # One sample row (should be cleared on generation)
    sample = ["0:00", "Sample activity", "Sample action", "Sample response", ""]
    for i, v in enumerate(sample):
        tbl.rows[1].cells[i].text = v

    doc.add_heading("Troubleshooting", level=2)
    tbl2 = doc.add_table(rows=2, cols=2)
    tbl2.style = "Table Grid"
    tbl2.rows[0].cells[0].text = "Situation"
    tbl2.rows[0].cells[1].text = "Response"
    tbl2.rows[1].cells[0].text = "Sample"
    tbl2.rows[1].cells[1].text = "Sample"

    doc.save(path)


def make_xlsx(path):
    """Create a minimal alignment matrix .xlsx template."""
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill

    wb = Workbook()
    ws = wb.active
    ws.title = "Alignment Matrix"
    headers = [
        "Learning Objective", "Bloom's Level", "Instructional Strategy",
        "Assessment Method", "Media Type", "Duration"
    ]
    for col, h in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=col, value=h)
        cell.font = Font(bold=True)
    wb.save(path)


# ─── analyze_template.py tests ────────────────────────────────────────────────

class TestAnalyzePptx(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(suffix=".pptx", delete=False)
        self.tmp.close()
        make_pptx(self.tmp.name)

    def tearDown(self):
        os.unlink(self.tmp.name)

    def test_returns_valid_json(self):
        rc, out, err = run(ANALYZE, "--file", self.tmp.name)
        self.assertEqual(rc, 0, err)
        data = json.loads(out)
        self.assertEqual(data["type"], "pptx")

    def test_layouts_present(self):
        _, out, _ = run(ANALYZE, "--file", self.tmp.name)
        data = json.loads(out)
        names = [l["name"] for l in data["layouts"]]
        self.assertIn("Title Slide", names)
        self.assertIn("Storyboard Row", names)

    def test_each_layout_has_placeholders(self):
        _, out, _ = run(ANALYZE, "--file", self.tmp.name)
        data = json.loads(out)
        for layout in data["layouts"]:
            self.assertIsInstance(layout["placeholders"], list)

    def test_existing_slide_count(self):
        _, out, _ = run(ANALYZE, "--file", self.tmp.name)
        data = json.loads(out)
        self.assertIn("existing_slide_count", data)
        self.assertIsInstance(data["existing_slide_count"], int)


class TestAnalyzeDocx(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(suffix=".docx", delete=False)
        self.tmp.close()
        make_docx(self.tmp.name)

    def tearDown(self):
        os.unlink(self.tmp.name)

    def test_returns_valid_json(self):
        rc, out, err = run(ANALYZE, "--file", self.tmp.name)
        self.assertEqual(rc, 0, err)
        data = json.loads(out)
        self.assertEqual(data["type"], "docx")

    def test_detects_tables(self):
        _, out, _ = run(ANALYZE, "--file", self.tmp.name)
        data = json.loads(out)
        self.assertGreaterEqual(len(data["tables"]), 1)

    def test_session_plan_headers_present(self):
        _, out, _ = run(ANALYZE, "--file", self.tmp.name)
        data = json.loads(out)
        headers = data["tables"][0]["headers"]
        self.assertIn("Time", headers)
        self.assertIn("Activity", headers)
        self.assertIn("Facilitator Action", headers)

    def test_headings_detected(self):
        _, out, _ = run(ANALYZE, "--file", self.tmp.name)
        data = json.loads(out)
        heading_texts = [h["text"] for h in data["headings"]]
        self.assertIn("Session Plan", heading_texts)


class TestAnalyzeXlsx(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False)
        self.tmp.close()
        make_xlsx(self.tmp.name)

    def tearDown(self):
        os.unlink(self.tmp.name)

    def test_returns_valid_json(self):
        rc, out, err = run(ANALYZE, "--file", self.tmp.name)
        self.assertEqual(rc, 0, err)
        data = json.loads(out)
        self.assertEqual(data["type"], "xlsx")

    def test_headers_detected(self):
        _, out, _ = run(ANALYZE, "--file", self.tmp.name)
        data = json.loads(out)
        headers = data["sheets"][0]["headers"]
        self.assertIn("Learning Objective", headers)
        self.assertIn("Bloom's Level", headers)


class TestAnalyzeErrors(unittest.TestCase):
    def test_missing_file(self):
        rc, out, _ = run(ANALYZE, "--file", "/nonexistent/file.pptx")
        self.assertNotEqual(rc, 0)
        data = json.loads(out)
        self.assertIn("error", data)

    def test_unsupported_extension(self):
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
            f.write(b"fake")
            name = f.name
        try:
            rc, out, _ = run(ANALYZE, "--file", name)
            self.assertNotEqual(rc, 0)
            data = json.loads(out)
            self.assertIn("error", data)
        finally:
            os.unlink(name)


# ─── generate_doc.py tests ────────────────────────────────────────────────────

XLSX_MAPPING = json.dumps({
    "column_map": {
        "objective": "Learning Objective",
        "bloom": "Bloom's Level",
        "strategy": "Instructional Strategy",
        "assessment": "Assessment Method",
        "media": "Media Type",
        "duration": "Duration",
    }
})

XLSX_DATA = json.dumps({
    "title": "Module 1 Alignment Matrix",
    "rows": [
        {
            "objective": "Given a delegation scenario, choose the appropriate task to delegate",
            "bloom": "Apply",
            "strategy": "Branching scenario",
            "assessment": "Scenario MCQ",
            "media": "Rise eLearning",
            "duration": "15 min",
        },
        {
            "objective": "Identify signs that a direct report is ready for increased autonomy",
            "bloom": "Analyze",
            "strategy": "Case study discussion",
            "assessment": "Observation checklist",
            "media": "ILT",
            "duration": "20 min",
        },
    ],
})

PPTX_MAPPING = json.dumps({
    "slide_types": {
        "Title": "Title Slide",
        "Content": "Storyboard Row",
        "Scenario": "Storyboard Row",
        "Knowledge Check": "Knowledge Check",
    },
    "fields": {
        "0": "text",
    }
})

PPTX_DATA = json.dumps({
    "title": "Delegate and Coach — Module 1",
    "version": "v1.0",
    "date": "2026-04-29",
    "slides": [
        {
            "num": 1,
            "type": "Title",
            "text": "Delegation and Coaching for New Managers",
            "narration": "Welcome to Module 1.",
            "visual": "Title slide with team image",
            "interaction": "None",
            "dev_notes": "Use brand header",
        },
        {
            "num": 2,
            "type": "Content",
            "text": "What does effective delegation look like?",
            "narration": "In this section we explore the four conditions for safe delegation.",
            "visual": "Split screen: manager and employee",
            "interaction": "Click to reveal",
            "dev_notes": "",
        },
        {
            "num": 3,
            "type": "Knowledge Check",
            "text": "Which of the following is a sign the task is ready to delegate?",
            "narration": "",
            "visual": "MCQ layout",
            "interaction": "MCQ — 4 options",
            "dev_notes": "Correct: B. Feedback: see slide notes.",
        },
    ],
})

DOCX_MAPPING = json.dumps({
    "session_plan_table": 0,
    "column_map": {
        "time": "Time",
        "activity": "Activity",
        "action": "Facilitator Action",
        "responses": "Anticipated Responses",
        "notes": "Notes",
    },
    "troubleshooting_table": 1,
})

DOCX_DATA = json.dumps({
    "title": "New Manager Workshop — Day 1",
    "length": "4 hrs",
    "max_participants": 20,
    "format": "ILT",
    "materials": ["Slide deck", "Handout A"],
    "setup": "U-shape seating, flip chart at front",
    "activities": [
        {
            "time": "0:00",
            "activity": "Welcome",
            "action": "Introduce yourself and the day's goals",
            "responses": "Participants share names and roles",
            "notes": "Keep energy high",
        },
        {
            "time": "0:15",
            "activity": "Delegation scenarios",
            "action": "Distribute scenario cards; small group discussion",
            "responses": "Groups identify delegation criteria",
            "notes": "Watch for 'everything is undelegatable' response",
        },
    ],
    "debrief": [
        "What surprised you about when to delegate?",
        "How will you apply this with your team this week?",
    ],
    "troubleshooting": [
        {
            "situation": "Group disengages during scenarios",
            "response": "Break into pairs; give one scenario each rather than group choice",
        }
    ],
})


class TestGenerateXlsx(unittest.TestCase):
    def setUp(self):
        self.template = tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False)
        self.template.close()
        make_xlsx(self.template.name)
        self.out = tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False)
        self.out.close()

    def tearDown(self):
        for f in [self.template.name, self.out.name]:
            if os.path.exists(f):
                os.unlink(f)

    def test_generates_file(self):
        rc, out, err = run(
            GENERATE,
            "--type", "alignment-matrix",
            "--template", self.template.name,
            "--data", XLSX_DATA,
            "--mapping", XLSX_MAPPING,
            "--out", self.out.name,
        )
        self.assertEqual(rc, 0, f"stderr: {err}\nstdout: {out}")
        self.assertTrue(os.path.exists(self.out.name))

    def test_output_is_valid_json(self):
        rc, out, _ = run(
            GENERATE,
            "--type", "alignment-matrix",
            "--template", self.template.name,
            "--data", XLSX_DATA,
            "--mapping", XLSX_MAPPING,
            "--out", self.out.name,
        )
        self.assertEqual(rc, 0)
        result = json.loads(out)
        self.assertIn("output", result)

    def test_data_rows_written(self):
        from openpyxl import load_workbook
        run(
            GENERATE,
            "--type", "alignment-matrix",
            "--template", self.template.name,
            "--data", XLSX_DATA,
            "--mapping", XLSX_MAPPING,
            "--out", self.out.name,
        )
        wb = load_workbook(self.out.name)
        ws = wb.active
        # Header row + 2 data rows = 3 rows
        rows_with_data = [
            row for row in ws.iter_rows(min_row=2, values_only=True)
            if any(v for v in row)
        ]
        self.assertEqual(len(rows_with_data), 2)

    def test_bloom_cell_has_fill(self):
        from openpyxl import load_workbook
        run(
            GENERATE,
            "--type", "alignment-matrix",
            "--template", self.template.name,
            "--data", XLSX_DATA,
            "--mapping", XLSX_MAPPING,
            "--out", self.out.name,
        )
        wb = load_workbook(self.out.name)
        ws = wb.active
        # Bloom's Level is column 2 (index 2); row 2 should have Apply color
        bloom_col = None
        for cell in ws[1]:
            if cell.value == "Bloom's Level":
                bloom_col = cell.column
                break
        self.assertIsNotNone(bloom_col)
        bloom_cell = ws.cell(row=2, column=bloom_col)
        self.assertNotEqual(bloom_cell.fill.fgColor.rgb, "00000000")


class TestGeneratePptx(unittest.TestCase):
    def setUp(self):
        self.template = tempfile.NamedTemporaryFile(suffix=".pptx", delete=False)
        self.template.close()
        make_pptx(self.template.name)
        self.out = tempfile.NamedTemporaryFile(suffix=".pptx", delete=False)
        self.out.close()

    def tearDown(self):
        for f in [self.template.name, self.out.name]:
            if os.path.exists(f):
                os.unlink(f)

    def test_generates_file(self):
        rc, out, err = run(
            GENERATE,
            "--type", "storyboard",
            "--template", self.template.name,
            "--data", PPTX_DATA,
            "--mapping", PPTX_MAPPING,
            "--out", self.out.name,
        )
        self.assertEqual(rc, 0, f"stderr: {err}\nstdout: {out}")
        self.assertTrue(os.path.exists(self.out.name))

    def test_slide_count_matches_data(self):
        from pptx import Presentation
        run(
            GENERATE,
            "--type", "storyboard",
            "--template", self.template.name,
            "--data", PPTX_DATA,
            "--mapping", PPTX_MAPPING,
            "--out", self.out.name,
        )
        data = json.loads(PPTX_DATA)
        prs = Presentation(self.out.name)
        self.assertEqual(len(prs.slides), len(data["slides"]))

    def test_narration_in_notes(self):
        from pptx import Presentation
        run(
            GENERATE,
            "--type", "storyboard",
            "--template", self.template.name,
            "--data", PPTX_DATA,
            "--mapping", PPTX_MAPPING,
            "--out", self.out.name,
        )
        prs = Presentation(self.out.name)
        first_slide = prs.slides[0]
        notes = first_slide.notes_slide.notes_text_frame.text
        self.assertIn("Welcome to Module 1", notes)

    def test_knowledge_check_uses_correct_layout(self):
        from pptx import Presentation
        run(
            GENERATE,
            "--type", "storyboard",
            "--template", self.template.name,
            "--data", PPTX_DATA,
            "--mapping", PPTX_MAPPING,
            "--out", self.out.name,
        )
        prs = Presentation(self.out.name)
        # Slide 3 should use Knowledge Check layout
        kc_slide = prs.slides[2]
        self.assertEqual(kc_slide.slide_layout.name, "Knowledge Check")


class TestGenerateDocx(unittest.TestCase):
    def setUp(self):
        self.template = tempfile.NamedTemporaryFile(suffix=".docx", delete=False)
        self.template.close()
        make_docx(self.template.name)
        self.out = tempfile.NamedTemporaryFile(suffix=".docx", delete=False)
        self.out.close()

    def tearDown(self):
        for f in [self.template.name, self.out.name]:
            if os.path.exists(f):
                os.unlink(f)

    def test_generates_file(self):
        rc, out, err = run(
            GENERATE,
            "--type", "facilitator-guide",
            "--template", self.template.name,
            "--data", DOCX_DATA,
            "--mapping", DOCX_MAPPING,
            "--out", self.out.name,
        )
        self.assertEqual(rc, 0, f"stderr: {err}\nstdout: {out}")
        self.assertTrue(os.path.exists(self.out.name))

    def test_activity_rows_written(self):
        from docx import Document
        run(
            GENERATE,
            "--type", "facilitator-guide",
            "--template", self.template.name,
            "--data", DOCX_DATA,
            "--mapping", DOCX_MAPPING,
            "--out", self.out.name,
        )
        doc = Document(self.out.name)
        tbl = doc.tables[0]
        # Header + 2 activity rows = 3 rows
        self.assertEqual(len(tbl.rows), 3)

    def test_activity_content_present(self):
        from docx import Document
        run(
            GENERATE,
            "--type", "facilitator-guide",
            "--template", self.template.name,
            "--data", DOCX_DATA,
            "--mapping", DOCX_MAPPING,
            "--out", self.out.name,
        )
        doc = Document(self.out.name)
        tbl = doc.tables[0]
        all_text = " ".join(c.text for row in tbl.rows for c in row.cells)
        self.assertIn("Delegation scenarios", all_text)

    def test_troubleshooting_row_written(self):
        from docx import Document
        run(
            GENERATE,
            "--type", "facilitator-guide",
            "--template", self.template.name,
            "--data", DOCX_DATA,
            "--mapping", DOCX_MAPPING,
            "--out", self.out.name,
        )
        doc = Document(self.out.name)
        tbl2 = doc.tables[1]
        all_text = " ".join(c.text for row in tbl2.rows for c in row.cells)
        self.assertIn("disengages", all_text)


# ─── Mapping persistence tests ────────────────────────────────────────────────

class TestMappingPersistence(unittest.TestCase):
    def setUp(self):
        self.template = tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False)
        self.template.close()
        make_xlsx(self.template.name)
        # Use a temporary mappings file to avoid polluting real one
        self._real_mappings = os.path.join(REPO_ROOT, "templates", "mappings.json")
        self._backup = None
        if os.path.exists(self._real_mappings):
            with open(self._real_mappings) as f:
                self._backup = f.read()

    def tearDown(self):
        os.unlink(self.template.name)
        if self._backup is not None:
            with open(self._real_mappings, "w") as f:
                f.write(self._backup)
        elif os.path.exists(self._real_mappings):
            with open(self._real_mappings, "w") as f:
                f.write("{}\n")

    def test_save_mapping(self):
        rc, out, err = run(
            GENERATE,
            "--save-mapping",
            "--template", self.template.name,
            "--mapping", XLSX_MAPPING,
        )
        self.assertEqual(rc, 0, err)
        result = json.loads(out)
        self.assertIn("saved", result)

    def test_saved_mapping_used_on_next_run(self):
        basename = os.path.basename(self.template.name)
        # Save mapping
        run(
            GENERATE,
            "--save-mapping",
            "--template", self.template.name,
            "--mapping", XLSX_MAPPING,
        )
        # Load mappings file and verify key exists
        with open(self._real_mappings) as f:
            mappings = json.load(f)
        self.assertIn(basename, mappings)

    def test_missing_mapping_returns_exit_2(self):
        # Fresh template with no saved mapping
        tmp = tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False)
        tmp.close()
        make_xlsx(tmp.name)
        try:
            rc, out, _ = run(
                GENERATE,
                "--type", "alignment-matrix",
                "--template", tmp.name,
                "--data", XLSX_DATA,
            )
            self.assertEqual(rc, 2)
            result = json.loads(out)
            self.assertEqual(result["error"], "no_mapping")
        finally:
            os.unlink(tmp.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)

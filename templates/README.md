# Templates

Place your custom document templates here. The skill will use them instead of
generating from scratch.

## Naming conventions

| File | Document type |
|---|---|
| `storyboard.pptx` | eLearning storyboard |
| `facilitator-guide.docx` | ILT/VILT facilitator guide |
| `alignment-matrix.xlsx` | Learning objective alignment matrix |

## How it works

1. **Add your template** — place the file here using the name above
2. **Analyze** — Claude runs `analyze_template.py` to read the structure
3. **Map** — Claude asks targeted questions to confirm which layout/column/heading
   maps to which content field; confirmed mappings are saved to `mappings.json`
4. **Confirm** — Claude shows what will be built (template, structure, output path)
5. **Generate** — `generate_doc.py` populates your template and writes to `generated/`

Mappings are saved in `mappings.json` (this directory) so future sessions skip
the interrogation step and go straight to confirmation.

## Template tips

### PowerPoint storyboard (.pptx)
- Name your slide layouts clearly — the mapping links layout names to slide types
  (Title, Content, Scenario, Knowledge Check)
- Narration always goes to the slide Notes field (standard PowerPoint convention)
- Additional fields (visual description, interaction, dev notes) go into the notes
  if no dedicated placeholder is mapped

### Word facilitator guide (.docx)
- Include the session plan as a table with clearly labeled column headers
  (Time, Activity, Facilitator Action, Anticipated Responses, Notes)
- A second table for troubleshooting (Situation | Response) is detected automatically
- Use Heading styles (Heading 1, Heading 2) for section structure

### Excel alignment matrix (.xlsx)
- First row must be the header row with column labels
- Column names can be anything — the mapping links them to the standard fields
  (objective, bloom, strategy, assessment, media, duration)
- Bloom's level cells are color-coded automatically on generation

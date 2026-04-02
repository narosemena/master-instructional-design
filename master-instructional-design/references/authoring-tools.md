# Authoring Tools — Expert Technical Reference

Load this file when the user is building in any eLearning authoring tool, needs code snippets, 
has technical questions about interactions, variables, publishing, or LMS integration.

---

## Table of Contents
1. Tool Selection Guide
2. Articulate Storyline 360 — Deep Technical Reference
3. Articulate Rise 360
4. Adobe Captivate
5. Lectora Inspire / Online
6. Camtasia
7. iSpring Suite
8. Other Tools (Evolent, Elucidat, Gomo, H5P)
9. JavaScript in eLearning — Master Reference
10. CSS Customization Techniques
11. SCORM / xAPI / LMS Integration
12. Accessibility & UDL in Authoring Tools

---

## 1. Tool Selection Guide

| Project Need | Best Tool |
|---|---|
| Complex branching, variables, custom interactions | Storyline 360 |
| Rapid development, responsive, modern UX | Rise 360 |
| Software simulations, responsive HTML5 | Adobe Captivate |
| Section 508 compliance priority | Lectora |
| Screen recording + video editing + quizzes | Camtasia |
| PowerPoint-to-eLearning conversion, VILT tools | iSpring Suite |
| Collaborative cloud authoring, enterprise | Elucidat / Gomo |
| Open-source / LMS-native content | H5P |

**Coaching principle**: Never let the tool drive the design. Choose the tool that best serves the learner experience and performance outcome — then use it to its fullest.

---

## 2. Articulate Storyline 360 — Deep Technical Reference

### Core Architecture
- **Scenes** → **Slides** → **Layers** (use layers for states, feedback, overlays — not new slides)
- **Master Slides**: Apply to all slides; use for nav, branding, persistent elements
- **Slide Masters vs Layout Masters**: Slide Masters are top-level; Layout Masters inherit from them
- **States**: Built-in (Normal, Hover, Visited, Selected, Disabled) + unlimited custom states
- **Variables**: True/False, Number, Text — the backbone of all custom logic

### Trigger System Best Practices
- Triggers fire top to bottom — order matters; always audit trigger order
- Use **conditions** on triggers to control logic flow (IF/AND/OR)
- Avoid trigger bloat: consolidate with variables instead of dozens of object-level triggers
- **"When timeline starts"** vs **"When timeline ends"** — pick intentionally
- Use **"Adjust Variable"** triggers to track learner progress across slides

### Variables — Advanced Patterns

**Progress tracking across scenes:**
```javascript
// Use a Number variable (e.g., "ProgressScore") 
// Increment by 1 on each slide's timeline start
// Show/hide completion elements when ProgressScore >= [target]
```

**Visited slide counter:**
- Create `SlidesVisited` (Number, default 0)
- On each required slide: Trigger → Adjust Variable → SlidesVisited += 1 → When timeline starts → Condition: SlidesVisited < [current slide number] (prevents double-counting on revisit)

**Branching with variables:**
- Create a Text variable (e.g., `UserPath`)
- Set value based on learner choices ("PathA", "PathB")
- Use conditions on navigation triggers to route accordingly

### JavaScript in Storyline (see Section 9 for full JS reference)

Access variables from JavaScript:
```javascript
var player = GetPlayer();
var myVar = player.GetVar("VariableName");
player.SetVar("VariableName", newValue);
```

Trigger JS via "Execute JavaScript" trigger — fires synchronously in the slide context.

### Layers — Best Practices
- Use layers for: feedback, tooltips, modal overlays, state-based content reveals
- **"Hide other slide layers"** checkbox: use carefully — it hides base layer too
- **"Prevent the user from clicking the base layer"** — essential for modal behavior
- Layers don't have their own timeline pause/resume by default — manage with triggers

### Slide Properties
- **"When revisiting"**: Always set intentionally — Reset to initial state / Resume saved state / Automatically decide
- For branching scenarios: "Resume saved state" preserves learner choices on back-navigation
- For knowledge checks: "Reset to initial state" ensures fresh attempt

### Motion Paths & Animation
- Entrance/exit animations: Use sparingly — cognitive load cost is real
- Motion paths: Powerful for interactive diagrams; combine with states for show/hide
- **Timing**: Sync animations to audio with the timeline; don't eyeball it

### Accessibility in Storyline
- Tab order: Customize via **Home → Accessibility** for every slide
- Alt text: Every image, every button, every interactive element
- **Focus order** must match visual reading order
- Closed captions: Use the built-in CC panel or import .vtt files
- Test with NVDA/JAWS; don't rely solely on Articulate's accessibility checker

---

## 3. Articulate Rise 360

### Architecture
- **Lessons** → **Blocks** (Rise is block-based — no slide paradigm)
- Blocks: Text, Image, Video, Quiz, Accordion, Tabs, Flashcards, Sorting, Matching, Button, Continue, Divider
- **Branching**: Use "Button" blocks + Lesson branching to create choose-your-path experiences

### Rise Customization (CSS via Custom Themes)
Rise doesn't expose CSS directly, but the **Theme** panel controls:
- Fonts (Google Fonts or custom upload)
- Brand colors (primary, secondary, accent)
- Button styles, cover styles

For CSS overrides: Use a **"Storyline block"** embedded in Rise with custom CSS injected via JS. This is the primary workaround for Rise's limited styling.

### Rise + Storyline Integration
- Embed Storyline interactions inside Rise as **Storyline blocks** (insert → Storyline)
- Best of both worlds: Rise's clean UX + Storyline's custom logic
- Sizing: Set Storyline slide to match Rise block dimensions (standard: 720×405 or 16:9 ratio)

### Rise Quiz Blocks
- Supports: Multiple choice, Multiple response, True/False, Fill-in-the-blank, Matching, Sorting, Hotspot
- **Knowledge checks** vs **Graded quizzes**: Knowledge checks don't report to LMS; graded quizzes do
- Pass/fail thresholds configurable per quiz block
- Cannot customize feedback beyond correct/incorrect at the block level — use Storyline for rich feedback

### Rise Publishing & LMS
- Publish as SCORM 1.2, SCORM 2004, xAPI, or web
- Completion tracking: By quiz score, by viewing all lessons, or by percentage of content viewed
- Rise is fully responsive — no separate mobile build needed

---

## 4. Adobe Captivate

### Strengths
- Best-in-class for **software simulations** (screen capture → click-through sim)
- Native **responsive design** with fluid boxes
- VR/360° content support
- Strong Section 508/WCAG compliance tooling

### Key Concepts
- **Responsive Project** vs **Blank Project**: Always start responsive unless targeting a fixed-size LMS
- **Fluid Boxes**: Responsive layout containers — use for all new projects
- **Object States**: Like Storyline states — Normal, Hover, Down, Visited + custom
- **Advanced Actions**: Storyline's equivalent of trigger+condition logic; use Standard or Conditional actions
- **Shared Actions**: Reusable action templates — massive time-saver for repetitive interactions

### Software Simulation Workflow
1. Record → Demo / Assessment / Training mode (choose intentionally)
2. Edit auto-generated slides; clean up unnecessary clicks
3. Add text captions, highlight boxes, click boxes
4. Training mode: learner performs actions; Assessment mode: scored simulation
5. Publish as HTML5 + SWF fallback (legacy) or HTML5 only (modern)

### JavaScript in Captivate
```javascript
// Access variables
var cpVar = window.cpAPIInterface.getVariableValue("varName");
window.cpAPIInterface.setVariableValue("varName", value);

// Execute on slide enter — use "On Enter" action with "Execute JavaScript"
```

### Captivate Publishing
- HTML5 output only recommended for all new projects (Flash is dead)
- SCORM 1.2 / 2004 / xAPI / cmi5
- Responsive output scales automatically; preview in multiple device sizes before publishing

---

## 5. Lectora Inspire / Online

### Strengths
- **Gold standard for Section 508 / WCAG 2.1 AA accessibility** — most compliant authoring tool
- Strong for **text-heavy, compliance-based training**
- Robust question library and test engine
- Lectora Online: Cloud-based collaborative authoring

### Key Concepts
- **Title → Chapters → Pages → Objects** (hierarchical structure — inheritance flows down)
- **Actions**: Lectora's trigger system (On: Click, Show, Hide, Run JavaScript, etc.)
- **Variables**: Global and local; use for tracking, branching, and personalization
- **Inherited Actions**: Set at Chapter or Title level; apply to all children — powerful for global nav

### Accessibility in Lectora
- Reading order panel: Drag to reorder for screen reader compliance
- Tab order: Separate from reading order — configure both
- Built-in WCAG checker; resolves most common issues automatically
- Alt text, ARIA labels, keyboard navigation all configurable without custom code

### JavaScript in Lectora
```javascript
// Get/set variables
var val = lectora.getVar("variableName");
lectora.setVar("variableName", newValue);
```

---

## 6. Camtasia

### Strengths
- Best for **screen recording + video editing + light interactivity**
- Ideal for: software tutorials, process walkthroughs, recorded webinars with added quizzes
- Lower development overhead than full authoring tools for video-based content

### Workflow
1. **Record**: Screen, webcam, audio (separately or together)
2. **Edit on timeline**: Cut, split, zoom-n-pan, annotations, callouts
3. **Enhance**: Add captions (auto-generate + edit), chapters, interactive hotspots
4. **Quiz**: Insert quiz questions at any point in the timeline (reports to SCORM/xAPI)
5. **Publish**: MP4, web, SCORM package, or Screencast.com hosting

### Camtasia Best Practices
- Record at 1920×1080; scale down if needed — never scale up
- Use **Zoom-n-Pan** to direct attention in software demos — reduces cognitive load
- Always generate and edit auto-captions — accuracy is ~85-90%, human review is essential
- **Callouts and annotations**: Use sparingly; they add extraneous load if overdone
- For SCORM: Publish via "Produce and Share" → LMS → choose SCORM version

---

## 7. iSpring Suite

### Strengths
- Works entirely **inside PowerPoint** — lowest barrier to entry
- Excellent for organizations heavily invested in PPT content
- Strong VILT tools: iSpring Space for collaborative review
- Dialogue simulations built into iSpring Suite Max

### Key Capabilities
- Convert PPT → HTML5 eLearning with animations preserved
- Built-in quiz maker (all question types, branching, randomization)
- Screen recording + video editor (lighter than Camtasia)
- Dialogue simulator for soft skills / conversation practice

### Limitations
- Design ceiling is PowerPoint's ceiling — encourage migration to dedicated tools for complex interactions
- Limited variable/logic capability vs. Storyline
- Not ideal for heavy branching or custom interaction patterns

---

## 8. Other Tools

| Tool | Best For |
|---|---|
| **Elucidat** | Enterprise collaborative authoring, brand-consistent at scale |
| **Gomo** | Responsive, cloud-based, strong analytics integration |
| **H5P** | Open-source, LMS-native (Moodle/Canvas), interactive video, free |
| **Evolent (formerly dominKnow)** | Responsive + fluid design, WCAG-strong, team authoring |
| **Synthesia** | AI avatar video — rapid video production without recording studio |
| **Canva for Education** | Visual job aids, infographics, supplementary materials |

---

## 9. JavaScript in eLearning — Master Reference

### Why Use JavaScript in Authoring Tools
- Extend beyond what the tool's native trigger/variable system supports
- Real-time calculations, dynamic text, date/time logic
- Integration with external data (LRS, APIs)
- Custom animations, DOM manipulation
- Persistent data storage (localStorage for non-LMS contexts)

### Storyline JavaScript Patterns

**Get/Set variables:**
```javascript
var player = GetPlayer();
// Read a variable
var score = player.GetVar("QuizScore");
// Set a variable
player.SetVar("QuizScore", score + 10);
// Set a text variable
player.SetVar("LearnerName", "Alex");
```

**Dynamic date/time stamp:**
```javascript
var player = GetPlayer();
var now = new Date();
var formatted = now.toLocaleDateString('en-US', {year:'numeric', month:'long', day:'numeric'});
player.SetVar("CompletionDate", formatted);
```

**Timer countdown:**
```javascript
var player = GetPlayer();
var timeLeft = player.GetVar("TimeRemaining"); // Number variable
timeLeft = timeLeft - 1;
player.SetVar("TimeRemaining", timeLeft);
if (timeLeft <= 0) {
  player.SetVar("TimerExpired", true);
}
// Call this via trigger: Execute JS every 1 second using a repeating timeline cue
```

**Randomize an array (for randomized scenarios):**
```javascript
var player = GetPlayer();
var items = ["Option A", "Option B", "Option C", "Option D"];
for (var i = items.length - 1; i > 0; i--) {
  var j = Math.floor(Math.random() * (i + 1));
  var temp = items[i];
  items[i] = items[j];
  items[j] = temp;
}
player.SetVar("RandomItem1", items[0]);
player.SetVar("RandomItem2", items[1]);
```

**LocalStorage for persistent data (non-LMS):**
```javascript
var player = GetPlayer();
// Save
localStorage.setItem("sl_progress", player.GetVar("ProgressScore"));
// Retrieve on course reopen
var saved = localStorage.getItem("sl_progress");
if (saved !== null) {
  player.SetVar("ProgressScore", parseInt(saved));
}
```

**Send custom xAPI statement from Storyline:**
```javascript
// Requires xAPI wrapper in your LMS or TinCan.js
var statement = {
  verb: { id: "http://adlnet.gov/expapi/verbs/completed" },
  object: { id: "https://yourorg.com/activities/module1", definition: { name: {"en-US": "Module 1"} } },
  result: { score: { scaled: GetPlayer().GetVar("FinalScore") / 100 } }
};
// Send via your LMS's xAPI endpoint — implement with TinCan.js or ADL xAPI wrapper
```

### CSS in Storyline / Rise

**Storyline — inject CSS via Execute JavaScript:**
```javascript
var style = document.createElement('style');
style.innerHTML = `
  .custom-button { background-color: #005A9C !important; border-radius: 8px !important; }
  .slide-title { font-family: 'Inter', sans-serif !important; font-size: 28px !important; }
`;
document.head.appendChild(style);
```

**Rise — inject via embedded Storyline block:**
Same CSS injection pattern via JS block; targets Rise's DOM classes (inspect to identify).

---

## 10. SCORM / xAPI / LMS Integration

### SCORM 1.2 vs SCORM 2004 vs xAPI — When to Use Which

| Standard | Use When |
|---|---|
| **SCORM 1.2** | Older LMS, maximum compatibility, simple completion/score tracking |
| **SCORM 2004** | Sequencing/navigation control, suspend data > 4096 chars needed |
| **xAPI (Tin Can)** | Modern LRS, granular learning data, mobile/offline, multi-system tracking |
| **cmi5** | xAPI + launch mechanism standard; best of both worlds; LMS must support |

### Common LMS Issues & Fixes
- **Suspend data truncation (SCORM 1.2)**: Limited to 4096 chars — reduce variable count or switch to SCORM 2004
- **Course won't mark complete**: Check completion trigger in tool matches LMS expectation (passed/completed vs viewed percentage)
- **Audio/video won't play**: LMS serving files with wrong MIME type — check server config or preload settings
- **Popup blocked**: LMS launching course in popup — use iframe launch option if available
- **Variables not saving on exit**: Ensure "SaveOnSuspend" or equivalent is configured; test exit vs suspend behavior

### xAPI Statement Design
Key verbs to know (ADL vocabulary):
- `experienced`, `attempted`, `completed`, `passed`, `failed`, `answered`, `interacted`, `progressed`

Design your xAPI statements intentionally — they are your learning data strategy. Ask: what do we need to know about how learners engage, and when?

---

## 11. Accessibility & UDL in Authoring Tools

### WCAG 2.1 AA — Core Requirements for eLearning
- **1.1.1** Alt text for all non-text content
- **1.2.2** Captions for all audio/video
- **1.3.1** Info/relationships conveyed through structure, not just visuals
- **1.4.3** Color contrast ≥ 4.5:1 (text) / 3:1 (large text)
- **2.1.1** All functionality keyboard accessible
- **2.4.3** Focus order logical and meaningful
- **4.1.2** Name, role, value for all UI components

### Tool-Specific Accessibility Quick Reference
- **Storyline**: Set tab order + focus order per slide; add alt text in object properties; test with NVDA
- **Rise**: Built-in responsive accessible; ensure all media has captions/descriptions; avoid color-only cues
- **Captivate**: Fluid boxes + accessibility panel; best native accessibility support of major tools
- **Lectora**: Gold standard; use built-in WCAG checker; reading order + tab order panels

### UDL Principles Applied to Authoring
- **Multiple Means of Representation**: Provide audio + text + visual versions of key content
- **Multiple Means of Action/Expression**: Offer keyboard nav, click, voice where possible
- **Multiple Means of Engagement**: Provide context/relevance, offer challenge calibration, support self-regulation

---

## Cross-References to Other Skill Files

- For **visual design principles** that govern what you build in these tools → `references/agile-and-design.md` §6–10
- For **JavaScript patterns** in Storyline used to implement xAPI statements → see §9 (JS Master Reference) above, and `references/generative-ai-for-ld.md` for AI-assisted code generation
- For **accessibility compliance** (WCAG, screen reader testing) in authoring tools → `references/agile-and-design.md` §11
- For **SCORM/xAPI strategy** at the LMS platform level → `references/lms-evaluation.md`
- For **Agile sprint workflow** for authoring tool development projects → `references/agile-and-design.md` §1–5


---
*© 2026 Norman Arosemena, CPTD. [CC BY-NC-ND 4.0](../../../LICENSE) — personal/educational use only; commercial use prohibited.*

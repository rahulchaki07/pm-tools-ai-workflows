# pm-tools-ai-workflows

**AI tools I use in my PM workflow — shared openly as working examples**

> Not a tutorial repo. These are tools I've built for myself that turned out to be useful to share. Each one solves a real workflow problem I had.

---

## The problem these solve

AI tools for PMs tend to be either:
1. Generic prompts in a doc that anyone could write, or
2. Heavy SaaS platforms with a 14-day free trial

I wanted something in the middle: working tools that do specific, valuable PM tasks, that I can adapt and run locally when I need them.

---

## Tools

### `prd_generator.py` — Structured PRD from discovery notes

Takes raw discovery notes (interview transcripts, user feedback, stakeholder requests) and produces a structured PRD skeleton with:
- Problem statement (synthesised from inputs)
- User segments and jobs-to-be-done
- Success metrics suggestions
- Scope and out-of-scope recommendations
- Open questions flagged for follow-up

**When I use this:** At the start of a new feature — takes 20 minutes of synthesis work and turns it into a structured starting point in ~30 seconds. I always edit the output heavily, but the skeleton saves time.

### `competitive_analysis.py` — Structured competitor teardown

Takes a product name and target category, searches for public information, and produces a structured analysis:
- Feature comparison matrix
- Positioning differences
- Pricing and packaging patterns
- Strategic gaps and opportunities

**When I use this:** For a quick read on a competitor before a sales call or investor meeting.

### `user_story_refiner.py` — Story quality checker

Takes a raw user story and checks it against a rubric:
- Is the user clearly defined?
- Is the job-to-be-done specific enough?
- Are acceptance criteria testable?
- Is the scope achievable in a sprint?

Returns the original story, a quality score, specific issues, and a rewritten version.

**When I use this:** Before sprint planning when I'm reviewing the backlog and stories feel vague.

### `interview_synthesiser.py` — Discovery interview analyser

Takes raw interview notes from multiple sessions and extracts:
- Themes across interviews
- Contradictions or tensions between user perspectives
- Jobs-to-be-done frequency ranking
- Direct quotes organised by theme

**When I use this:** After a round of discovery interviews before synthesising into a problem brief.

---

## File structure

```
pm-tools-ai-workflows/
├── README.md
├── prd_generator.py          
├── competitive_analysis.py   
├── user_story_refiner.py     
├── interview_synthesiser.py  
├── prompts/
│   ├── prd_system.txt        # System context for PRD generation
│   ├── competitive_system.txt
│   ├── story_system.txt
│   └── interview_system.txt
├── examples/
│   ├── sample_discovery_notes.txt     # Anonymised sample input
│   ├── sample_prd_output.md           # Example PRD skeleton output
│   └── sample_interview_synthesis.md  # Example synthesis output
└── config.py                 # Model and prompt configuration
```

---

## Setup

```bash
pip install anthropic python-dotenv

# Create .env file
echo "ANTHROPIC_API_KEY=your_key_here" > .env
```

---

## Usage

```bash
# Generate PRD skeleton from discovery notes
python prd_generator.py --input examples/sample_discovery_notes.txt

# Analyse competitor
python competitive_analysis.py --product "Icertis" --category "CLM"

# Check user story quality
python user_story_refiner.py --story "As a user I want to see contracts"

# Synthesise interviews
python interview_synthesiser.py --input-dir ./interview_notes/
```

---

## Design decisions worth noting

**Why local scripts, not a SaaS tool?**
I want control over what data I'm sending to which model. Discovery interview notes and PRD content contain sensitive strategic information. Running locally means I control the data.

**Why Claude API and not ChatGPT?**
I've tested both. For structured extraction and synthesis tasks (the core of what these tools do), the instruction-following quality is meaningfully better. For creative writing tasks the gap is smaller.

**Why no fancy UI?**
Because the 30-second effort to run a terminal script is fine when the output is valuable. UI complexity would distract from the actual output. If a tool is worth having a UI, it's worth productising properly — otherwise terminal is fine.

---

## A note on AI tools for PMs

These tools are force multipliers, not replacements. The PRD generator doesn't write PRDs — I do. It helps me not stare at a blank page. The interview synthesiser doesn't do discovery analysis — I do. It helps me see patterns I might miss when I'm reading 8 transcripts in a row.

The skill is knowing what to prompt, how to evaluate the output, and what to change. That's still a human skill.

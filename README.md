# pm-tools-ai-workflows

[![CI](https://github.com/rahulchaki/pm-tools-ai-workflows/actions/workflows/ci.yml/badge.svg)](https://github.com/rahulchaki/pm-tools-ai-workflows/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

AI-assisted PM workflows I use in real product work, packaged as local scripts.

This repo is designed to be practical and easy to inspect:
- clear prompts
- simple command-line tools
- realistic examples
- structured outputs you can edit into real product docs

---

## What this project is (in plain English)

This project gives Product Managers four practical AI helpers:
1. turn messy discovery notes into a PRD draft
2. create a competitor analysis draft
3. improve weak user stories
4. summarize many interview notes into themes

You run everything locally from your terminal.  
No fancy UI, no lock-in, full prompt visibility.

---

## Start in 3 steps

```bash
# 1) Install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2) Add your API key
echo "ANTHROPIC_API_KEY=your_key_here" > .env

# 3) Run one tool
python prd_generator.py \
  --input examples/sample_discovery_notes.txt \
  --output outputs/prd.md
```

Then compare your output with: `examples/sample_prd_output.md`

---

## Tools (what each one does)

### `prd_generator.py`
Creates a PRD skeleton from raw discovery notes.

**Good for:** starting feature planning quickly.

### `competitive_analysis.py`
Creates a competitor teardown from a product name and category.

**Good for:** sales prep, strategy discussions, investor prep.

### `user_story_refiner.py`
Scores and rewrites a weak user story.

**Good for:** sprint planning and backlog quality.

### `interview_synthesiser.py`
Summarizes many interview files into themes and insights.

**Good for:** discovery synthesis and problem framing.

---

## Project map (easy file guide)

If you are new, read this first: `FILE_GUIDE.md`

| File/Folder | What it means |
|---|---|
| `README.md` | Main guide: what this repo does and how to run it |
| `FILE_GUIDE.md` | Plain-English explanation of every important file |
| `config.py` | Shared setup used by all tools (API key, prompt loading, model call) |
| `prd_generator.py` | PRD draft tool |
| `competitive_analysis.py` | Competitor analysis tool |
| `user_story_refiner.py` | User story quality/refinement tool |
| `interview_synthesiser.py` | Interview synthesis tool |
| `prompts/` | Detailed system prompts used by each tool |
| `examples/` | Sample input and portfolio-quality sample outputs |
| `tests/` | Basic tests that verify core behavior |
| `.github/workflows/ci.yml` | GitHub Action that runs tests automatically |
| `requirements.txt` | Python dependencies |
| `Makefile` | Shortcut commands (`make test`, `make demo-prd`, etc.) |
| `LICENSE` | Open-source license |

---

## Folder structure

```text
pm-tools-ai-workflows/
├── README.md
├── FILE_GUIDE.md
├── LICENSE
├── Makefile
├── requirements.txt
├── .gitignore
├── config.py
├── prd_generator.py
├── competitive_analysis.py
├── user_story_refiner.py
├── interview_synthesiser.py
├── prompts/
│   ├── prd_system.txt
│   ├── competitive_system.txt
│   ├── story_system.txt
│   └── interview_system.txt
├── examples/
│   ├── README.md
│   ├── sample_discovery_notes.txt
│   ├── sample_prd_output.md
│   ├── sample_interview_synthesis.md
│   ├── sample_competitive_analysis_output.md
│   └── sample_story_refinement_output.md
├── screenshots/
│   └── README.md
├── tests/
│   └── test_core.py
└── .github/
    └── workflows/
        └── ci.yml
```

---

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo "ANTHROPIC_API_KEY=your_key_here" > .env
```

Quick setup via Make:

```bash
make setup
```

---

## Usage

All tools support:
- `--output` to write markdown to file
- `--model` to override model (optional)
- `--max-tokens` to control output length (optional)

```bash
# Generate PRD skeleton
python prd_generator.py \
  --input examples/sample_discovery_notes.txt \
  --output outputs/prd.md

# Competitive analysis
python competitive_analysis.py \
  --product "Icertis" \
  --category "CLM" \
  --output outputs/competitive.md

# User story refinement
python user_story_refiner.py \
  --story "As a user I want to see contracts" \
  --output outputs/story.md

# Interview synthesis
python interview_synthesiser.py \
  --input-dir ./interview_notes/ \
  --output outputs/interview_synthesis.md
```

Makefile shortcuts:

```bash
make demo-prd
make demo-competitive
make demo-story
make demo-interview
```

---

## Examples

See `examples/README.md` for a guided walkthrough and expected outputs.

Portfolio-ready artifacts included:
- `examples/sample_prd_output.md`
- `examples/sample_interview_synthesis.md`
- `examples/sample_competitive_analysis_output.md`
- `examples/sample_story_refinement_output.md`

---

## Screenshots for portfolio

- Add visual proof in `screenshots/` (see `screenshots/README.md` for suggested files).
- Include at least one terminal run screenshot and one output screenshot per tool.
- Keep screenshots anonymized and consistent in style.

---

## Quality and reliability

- Prompt templates are detailed and structured for consistency.
- API calls use simple retry backoff for transient failures.
- Unit tests cover core behavior and input handling.
- GitHub Actions CI runs tests on push/PR.

Run tests locally:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

---

## Limitations

- These are drafting and synthesis aids, not final artifacts.
- Output quality depends on input quality and coverage.
- Competitive analysis should be validated with primary research before major decisions.
- Human PM judgment is always required before shipping decisions.

---

## Who this is for

- PMs who want practical AI workflows, not generic prompts
- founders and operators who need structured drafts quickly
- learners building PM + AI portfolio projects

If you are evaluating this repo on GitHub, start with:
1. `README.md`
2. `FILE_GUIDE.md`
3. `examples/README.md`

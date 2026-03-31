# File Guide (Plain English)

This guide explains what each important file does so even non-engineers can understand the project quickly.

## Core scripts

- `prd_generator.py`  
  Takes discovery notes and creates a first-draft PRD structure.

- `competitive_analysis.py`  
  Takes a competitor name + market category and creates a strategy-style comparison output.

- `user_story_refiner.py`  
  Takes one raw user story and scores/rewrites it into clearer, testable format.

- `interview_synthesiser.py`  
  Reads multiple interview-note files and summarizes themes, tensions, and product implications.

## Shared logic

- `config.py`  
  Shared utility file used by all scripts. Handles:
  - reading API key from `.env`
  - loading prompt files
  - calling the AI model
  - basic retry for temporary API failures

## Prompt templates

All prompt files live in `prompts/`:

- `prompts/prd_system.txt` -> instructions for PRD generation
- `prompts/competitive_system.txt` -> instructions for competitor analysis
- `prompts/story_system.txt` -> instructions for user story quality scoring/refinement
- `prompts/interview_system.txt` -> instructions for interview synthesis

These are the most important files for output quality.

## Example artifacts

All sample files live in `examples/`:

- `sample_discovery_notes.txt` -> sample input notes
- `sample_prd_output.md` -> expected style of PRD output
- `sample_interview_synthesis.md` -> expected style of synthesis output
- `sample_competitive_analysis_output.md` -> expected style of competitor output
- `sample_story_refinement_output.md` -> expected style of story refinement output
- `examples/README.md` -> how to walk through examples

## Project and quality files

- `README.md` -> top-level project guide
- `requirements.txt` -> dependencies to install
- `.gitignore` -> files that should not be committed (`.env`, cache files, etc.)
- `tests/test_core.py` -> simple checks to ensure core functions behave correctly
- `.github/workflows/ci.yml` -> automatically runs tests on GitHub
- `Makefile` -> command shortcuts (`make test`, `make demo-prd`, etc.)
- `LICENSE` -> open-source license (MIT)

## Typical flow for a new user

1. Read `README.md`
2. Add API key to `.env`
3. Run one script with sample input
4. Compare generated output with files in `examples/`
5. Edit prompts in `prompts/` to match your own style

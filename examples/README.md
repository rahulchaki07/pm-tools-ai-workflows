# Examples Index

This folder contains portfolio-grade sample artifacts that show realistic PM workflows and output quality.

## Inputs

- `sample_discovery_notes.txt`
  - Discovery packet style notes (interviews, support signals, sales signals, constraints).
  - Use with: `prd_generator.py`

## Outputs

- `sample_prd_output.md`
  - Structured PRD skeleton generated from discovery notes.
  - Showcases scope, metrics, risks, and a short execution plan.

- `sample_interview_synthesis.md`
  - Multi-interview synthesis with themes, contradictions, JTBD ranking, and validation plan.
  - Mirrors what a PM/research pre-read might look like.

- `sample_competitive_analysis_output.md`
  - Competitor teardown with confidence labels, strategy implications, and a 30-day action plan.

- `sample_story_refinement_output.md`
  - User story quality review with rubric scoring, rewritten story, and Given/When/Then criteria.

## Suggested Demo Flow

1. Start with `sample_discovery_notes.txt`
2. Generate PRD using `prd_generator.py`
3. Compare generated output to `sample_prd_output.md`
4. Run other tools and compare against their sample outputs

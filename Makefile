PYTHON ?= python3

.PHONY: setup test demo-prd demo-competitive demo-story demo-interview

setup:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m unittest discover -s tests -p "test_*.py"

demo-prd:
	$(PYTHON) prd_generator.py --input examples/sample_discovery_notes.txt --output outputs/prd.md

demo-competitive:
	$(PYTHON) competitive_analysis.py --product "Icertis" --category "CLM" --output outputs/competitive.md

demo-story:
	$(PYTHON) user_story_refiner.py --story "As a user I want to see contracts" --output outputs/story.md

demo-interview:
	$(PYTHON) interview_synthesiser.py --input-dir interview_notes --output outputs/interview_synthesis.md

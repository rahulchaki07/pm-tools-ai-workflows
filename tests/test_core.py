from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from competitive_analysis import build_user_prompt as competitor_prompt
from config import read_prompt
from interview_synthesiser import collect_notes
from prd_generator import build_user_prompt as prd_prompt
from user_story_refiner import build_user_prompt as story_prompt


class TestCoreBehavior(unittest.TestCase):
    def test_read_prompt_existing(self) -> None:
        text = read_prompt("prd_system.txt")
        self.assertIn("PRD", text)

    def test_read_prompt_missing_raises(self) -> None:
        with self.assertRaises(FileNotFoundError):
            read_prompt("does_not_exist.txt")

    def test_collect_notes_from_directory(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "a.txt").write_text("first note", encoding="utf-8")
            (root / "b.md").write_text("second note", encoding="utf-8")
            combined = collect_notes(root)

            self.assertIn("Interview File: a.txt", combined)
            self.assertIn("Interview File: b.md", combined)
            self.assertIn("first note", combined)
            self.assertIn("second note", combined)

    def test_collect_notes_empty_directory_raises(self) -> None:
        with TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                collect_notes(Path(tmp))

    def test_prompt_builders_embed_inputs(self) -> None:
        self.assertIn("Discovery notes", prd_prompt("notes"))
        self.assertIn("Product name: Icertis", competitor_prompt("Icertis", "CLM"))
        self.assertIn("User story:", story_prompt("As a user..."))


if __name__ == "__main__":
    unittest.main()

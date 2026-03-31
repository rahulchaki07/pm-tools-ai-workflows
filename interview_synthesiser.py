"""Synthesise discovery interview notes across multiple sessions."""

from __future__ import annotations

import argparse
from pathlib import Path

from config import call_claude, read_prompt


def collect_notes(input_dir: Path) -> str:
    files = sorted(
        [
            path
            for path in input_dir.iterdir()
            if path.is_file() and path.suffix.lower() in {".txt", ".md"}
        ]
    )
    if not files:
        raise ValueError(
            f"No .txt or .md interview note files found in directory: {input_dir}"
        )

    combined = []
    for file_path in files:
        combined.append(f"## Interview File: {file_path.name}\n")
        combined.append(file_path.read_text(encoding="utf-8").strip())
        combined.append("\n")
    return "\n".join(combined).strip()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Synthesise interview notes across a directory."
    )
    parser.add_argument(
        "--input-dir",
        required=True,
        help="Directory containing interview note files (.txt or .md).",
    )
    parser.add_argument(
        "--output",
        help="Optional output markdown file path. Prints to stdout if omitted.",
    )
    parser.add_argument("--model", help="Optional Claude model override.")
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=1500,
        help="Maximum tokens in the model response.",
    )
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    if not input_dir.exists() or not input_dir.is_dir():
        raise NotADirectoryError(f"Input directory not found: {input_dir}")

    notes_blob = collect_notes(input_dir)
    system_prompt = read_prompt("interview_system.txt")
    user_prompt = (
        "Synthesise the interview notes below.\n\n"
        f"{notes_blob}\n"
    )
    result = call_claude(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        model=args.model,
        max_tokens=args.max_tokens,
    )

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(result, encoding="utf-8")
        print(f"Interview synthesis written to: {output_path}")
        return

    print(result)


if __name__ == "__main__":
    main()

"""Generate a structured PRD skeleton from discovery notes."""

from __future__ import annotations

import argparse
from pathlib import Path

from config import call_claude, read_prompt


def build_user_prompt(discovery_notes: str) -> str:
    return (
        "Use the discovery notes below to generate a structured PRD skeleton.\n\n"
        "Discovery notes:\n"
        f"{discovery_notes}\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a structured PRD skeleton from discovery notes."
    )
    parser.add_argument("--input", required=True, help="Path to discovery notes text file.")
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

    input_path = Path(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    notes = input_path.read_text(encoding="utf-8")
    system_prompt = read_prompt("prd_system.txt")
    result = call_claude(
        system_prompt=system_prompt,
        user_prompt=build_user_prompt(notes),
        model=args.model,
        max_tokens=args.max_tokens,
    )

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(result, encoding="utf-8")
        print(f"PRD skeleton written to: {output_path}")
        return

    print(result)


if __name__ == "__main__":
    main()

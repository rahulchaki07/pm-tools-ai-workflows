"""Shared configuration and helper utilities for PM AI tools."""

from __future__ import annotations

import os
import time
from pathlib import Path
from typing import Optional

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - optional for local env convenience
    load_dotenv = None  # type: ignore[assignment]

try:
    from anthropic import Anthropic
except ImportError:  # pragma: no cover - import is validated at runtime by usage
    Anthropic = None  # type: ignore[assignment]


DEFAULT_MODEL = "claude-3-5-sonnet-latest"
DEFAULT_MAX_TOKENS = 1500
PROMPTS_DIR = Path(__file__).parent / "prompts"


def load_env() -> None:
    """Load environment variables from .env if present."""
    if load_dotenv is not None:
        load_dotenv()


def read_prompt(prompt_filename: str) -> str:
    """Read a prompt file from the prompts directory."""
    path = PROMPTS_DIR / prompt_filename
    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {path}")
    return path.read_text(encoding="utf-8")


def get_anthropic_client() -> "Anthropic":
    """Return an Anthropic client configured from environment."""
    if Anthropic is None:
        raise RuntimeError(
            "anthropic package is not installed. Run: pip install anthropic python-dotenv"
        )

    load_env()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError(
            "ANTHROPIC_API_KEY is missing. Add it to your environment or .env file."
        )

    return Anthropic(api_key=api_key)


def call_claude(
    *,
    system_prompt: str,
    user_prompt: str,
    model: Optional[str] = None,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    max_retries: int = 2,
) -> str:
    """Call Claude with a system prompt and user content."""
    client = get_anthropic_client()
    attempt = 0
    while True:
        try:
            response = client.messages.create(
                model=model or DEFAULT_MODEL,
                max_tokens=max_tokens,
                system=system_prompt,
                messages=[{"role": "user", "content": user_prompt}],
            )
            break
        except Exception:
            if attempt >= max_retries:
                raise
            # Simple backoff for transient API/network failures.
            time.sleep(1 + attempt)
            attempt += 1

    chunks = []
    for block in response.content:
        text = getattr(block, "text", None)
        if text:
            chunks.append(text)
    return "\n".join(chunks).strip()

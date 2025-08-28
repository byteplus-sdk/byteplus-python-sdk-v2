from typing import Optional

from pydantic import BaseModel

__all__ = ["MultimodalEmbeddingUsage", "PromptTokensDetails"]


class PromptTokensDetails(BaseModel):
    text_tokens: int
    """Number of tokens in the text."""
    image_tokens: int
    """Number of tokens in the image."""


class MultimodalEmbeddingUsage(BaseModel):
    prompt_tokens: int
    """Number of tokens in the prompt."""

    total_tokens: int
    """Total number of tokens used in the request (prompt + completion)."""

    prompt_tokens_details: Optional[PromptTokensDetails] = None
    """Prompt tokens details."""

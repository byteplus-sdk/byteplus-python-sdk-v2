from typing import Optional

from byteplussdkarkruntime._models import BaseModel


class ContentGenerationTaskID(BaseModel):
    id: str
    """A unique identifier for the task."""

    safety_identifier: Optional[str] = None
    """The safety identifier associated with the task."""

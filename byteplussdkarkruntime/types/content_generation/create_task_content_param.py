from __future__ import annotations

from typing import Union

from typing_extensions import Literal, TypedDict

__all__ = [
    "CreateTaskContentTextParam",
    "CreateTaskContentImageDataParam",
    "CreateTaskContentAudioDataParam",
    "CreateTaskContentVideoDataParam",
    "CreateTaskContentImageParam",
    "CreateTaskContentAudioParam",
    "CreateTaskContentVideoParam",
    "CreateTaskContentParam",
]


class CreateTaskContentTextParam(TypedDict):
    type: Literal["text"]
    text: str
    """Text prompt describing the video generation job."""


class CreateTaskContentImageDataParam(TypedDict):
    url: str
    """URL of the image to be used for content generation."""


class CreateTaskContentAudioDataParam(TypedDict):
    url: str
    """URL of the audio to be used for content generation."""


class CreateTaskContentVideoDataParam(TypedDict):
    url: str
    """URL of the video to be used for content generation."""


class CreateTaskContentImageParam(TypedDict):
    type: Literal["image_url"]
    image_url: CreateTaskContentImageDataParam
    role: str
    """Image data object containing image URL."""


class CreateTaskContentAudioParam(TypedDict):
    type: Literal["audio_url"]
    audio_url: CreateTaskContentAudioDataParam
    role: str
    """Audio data object containing audio URL."""


class CreateTaskContentVideoParam(TypedDict):
    type: Literal["video_url"]
    video_url: CreateTaskContentVideoDataParam
    role: str
    """Video data object containing video URL."""


class CreateTaskContentDraftTaskParam(TypedDict):
    type: Literal["draft_task"]
    draft_task: CreateTaskContentDraftTaskDataParam
    """ID of the draft task to be used for content generation."""


class CreateTaskContentDraftTaskDataParam(TypedDict):
    id: str
    """ID of the draft task to be used for content generation."""


CreateTaskContentParam = Union[CreateTaskContentTextParam, CreateTaskContentImageParam, CreateTaskContentAudioParam, CreateTaskContentVideoParam, CreateTaskContentDraftTaskParam]

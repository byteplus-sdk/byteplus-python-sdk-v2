import unittest

from byteplussdkarkruntime._compat import field_outer_type, get_model_fields, model_parse
from byteplussdkarkruntime.types.content_generation.content_generation_task import (
    ContentGenerationTask,
)


def _task_payload(**overrides):
    payload = {
        "id": "task-id",
        "model": "test-model",
        "status": "succeeded",
        "error": {"message": "", "code": ""},
        "content": {
            "video_url": "https://example.com/video.mp4",
            "last_frame_url": "https://example.com/frame.png",
            "file_url": "https://example.com/output.zip",
        },
        "usage": {"completion_tokens": 1},
        "subdivisionlevel": "default",
        "fileformat": "mp4",
        "frames": 120,
        "framespersecond": 30,
        "created_at": 1,
        "updated_at": 2,
        "seed": 3,
        "revised_prompt": "prompt",
        "service_tier": "default",
        "execution_expires_after": 3600,
        "priority": 0,
        "generate_audio": False,
        "duration": 4,
        "ratio": "16:9",
        "resolution": "1080p",
        "draft": False,
        "draft_task_id": "",
    }
    payload.update(overrides)
    return payload


class ContentGenerationTaskFieldsTest(unittest.TestCase):
    def test_output_format_is_a_declared_model_field(self):
        self.assertIn("output_format", get_model_fields(ContentGenerationTask))

    def test_output_format_is_parsed_and_duration_stays_integer(self):
        duration_field = get_model_fields(ContentGenerationTask)["duration"]
        task = model_parse(
            ContentGenerationTask,
            _task_payload(output_format="mp4"),
        )

        self.assertEqual(task.output_format, "mp4")
        self.assertIs(field_outer_type(duration_field), int)
        self.assertEqual(task.duration, 4)
        self.assertIs(type(task.duration), int)

    def test_output_format_defaults_to_none(self):
        task = model_parse(ContentGenerationTask, _task_payload())

        self.assertIsNone(task.output_format)


if __name__ == "__main__":
    unittest.main()

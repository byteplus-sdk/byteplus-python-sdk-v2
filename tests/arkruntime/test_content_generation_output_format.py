import asyncio
import unittest

from byteplussdkarkruntime.resources.content_generation.tasks import AsyncTasks, Tasks


class _SyncClient:
    api_key = "test-api-key"

    def __init__(self):
        self.request = None

    def post(self, path, **kwargs):
        self.request = (path, kwargs)
        return object()

    get = delete = post_without_retry = get_api_list = post


class _AsyncClient:
    api_key = "test-api-key"

    def __init__(self):
        self.request = None

    async def post(self, path, **kwargs):
        self.request = (path, kwargs)
        return object()

    get = delete = post_without_retry = get_api_list = post


class ContentGenerationCreateFieldsTest(unittest.TestCase):
    def test_sync_create_sends_output_format_and_omni_reference_task_type(self):
        client = _SyncClient()

        Tasks(client).create(
            model="test-model",
            content=[],
            output_format="mp4",
            omni_reference_task_type="reference_video",
        )

        self.assertEqual(client.request[0], "/contents/generations/tasks")
        self.assertEqual(client.request[1]["body"]["output_format"], "mp4")
        self.assertEqual(
            client.request[1]["body"]["omni_reference_task_type"],
            "reference_video",
        )

    def test_sync_create_defaults_new_fields_to_none(self):
        client = _SyncClient()

        Tasks(client).create(model="test-model", content=[])

        self.assertIsNone(client.request[1]["body"]["output_format"])
        self.assertIsNone(client.request[1]["body"]["omni_reference_task_type"])

    def test_async_create_sends_output_format_and_omni_reference_task_type(self):
        client = _AsyncClient()

        asyncio.run(
            AsyncTasks(client).create(
                model="test-model",
                content=[],
                output_format="gif",
                omni_reference_task_type="reference_image",
            )
        )

        self.assertEqual(client.request[0], "/contents/generations/tasks")
        self.assertEqual(client.request[1]["body"]["output_format"], "gif")
        self.assertEqual(
            client.request[1]["body"]["omni_reference_task_type"],
            "reference_image",
        )

    def test_async_create_defaults_new_fields_to_none(self):
        client = _AsyncClient()

        asyncio.run(AsyncTasks(client).create(model="test-model", content=[]))

        self.assertIsNone(client.request[1]["body"]["output_format"])
        self.assertIsNone(client.request[1]["body"]["omni_reference_task_type"])


if __name__ == "__main__":
    unittest.main()

import asyncio
import sys
from datetime import datetime

from byteplussdkarkruntime import AsyncArk

# Authentication
# 1.If you authorize your endpoint using an API key, you can set your api key to environment variable "ARK_API_KEY"
# or specify api key by Ark(api_key="${YOUR_API_KEY}").
# Note: If you use an API key, this API key will not be refreshed.
# To prevent the API from expiring and failing after some time, choose an API key with no expiration date.

# 2.If you authorize your endpoint with Byteplus Identity and Access Management（IAM), set your api key to environment variable "BYTEPLUS_ACCESSKEY", "BYTEPLUS_SECRETKEY"
# or specify ak&sk by Ark(ak="${YOUR_AK}", sk="${YOUR_SK}").
# To get your ak&sk, please refer to this document(https://docs.byteplus.com/en/docs/byteplus-platform/docs-creating-an-accesskey)
# For more information，please check this document（https://docs.byteplus.com/en/docs/ModelArk/1361424）


async def worker(
    worker_id: int,
    client: AsyncArk,
    requests: asyncio.Queue[dict],
):
    print(f"Worker {worker_id} is starting.")

    while True:
        request = await requests.get()
        try:
            completion = await client.batch_chat.completions.create(**request)
            print(completion)
        except Exception as e:
            print(e, file=sys.stderr)
        finally:
            requests.task_done()


async def main():
    start = datetime.now()
    max_concurrent_tasks, task_num = 1000, 10000

    requests = asyncio.Queue()
    client = AsyncArk(timeout=24 * 3600)

    # mock `task_num` tasks
    for _ in range(task_num):
        await requests.put(
            {
                "model": "${YOUR_ENDPOINT_ID}",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a helpful AI assistant.",
                    },
                    {"role": "user", "content": "Hello, How are you?"},
                ],
            }
        )

    # create `max_concurrent_tasks` workers and start them
    tasks = [
        asyncio.create_task(worker(i, client, requests))
        for i in range(max_concurrent_tasks)
    ]

    # wait for all requests is done
    await requests.join()

    # stop workers
    for task in tasks:
        task.cancel()

    # wait for all workers is canceled
    await asyncio.gather(*tasks, return_exceptions=True)
    await client.close()

    end = datetime.now()
    print(f"Total time: {end - start}, Total task: {task_num}")


if __name__ == "__main__":
    asyncio.run(main())

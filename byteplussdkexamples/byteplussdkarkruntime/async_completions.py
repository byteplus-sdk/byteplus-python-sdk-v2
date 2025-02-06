import asyncio

from byteplussdkarkruntime import AsyncArk

# Authentication
# 1.If you authorize your endpoint using an API key, you can set your api key to environment variable "ARK_API_KEY"
# or specify api key by Ark(api_key="${YOUR_API_KEY}").
# Note: If you use an API key, this API key will not be refreshed.
# To prevent the API from expiring and failing after some time, choose an API key with no expiration date.

# 2.If you authorize your endpoint with Identity and Access Management（IAM), set your api key to environment variable "BYTEPLUS_ACCESSKEY", "BYTEPLUS_SECRETKEY"
# or specify ak&sk by Ark(ak="${YOUR_AK}", sk="${YOUR_SK}").
# To get your ak&sk, please refer to this document(https://www.volcengine.com/docs/6291/65568)
# For more information，please check this document（https://www.volcengine.com/docs/82379/1263279）
client = AsyncArk()


async def main():
    stream = await client.chat.completions.create(
        model="",
        messages=[
            {"role": "system", "content": "You are Francis, a helpful AI assistant."},
            {"role": "user", "content": "How are you today?"},
        ],
        stream=True
    )
    async for completion in stream:
        print(completion.choices[0].delta.content, end="")


if __name__ == "__main__":
    asyncio.run(main())

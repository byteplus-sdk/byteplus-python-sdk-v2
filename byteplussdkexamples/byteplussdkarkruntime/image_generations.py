from byteplussdkarkruntime import Ark

# Authentication
# 1.If you authorize your endpoint using an API key, you can set your api key to environment variable "ARK_API_KEY"
# or specify api key by Ark(api_key="${YOUR_API_KEY}").
# Note: If you use an API key, this API key will not be refreshed.
# To prevent the API from expiring and failing after some time, choose an API key with no expiration date.
client = Ark()

if __name__ == "__main__":
    print("----- generate images -----")

    result = client.images.generate(
        model="${YOUR_ENDPOINT_ID}",
        prompt="Bird soaring above vast grasslands",
        seed=1234567890,
        watermark=True,
        size="512x512",
        guidance_scale=2.5,
    )

    print(result)

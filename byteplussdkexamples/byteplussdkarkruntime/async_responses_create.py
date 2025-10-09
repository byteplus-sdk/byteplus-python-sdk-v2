import asyncio

from byteplussdkarkruntime import AsyncArk
from byteplussdkarkruntime.types.responses.response_completed_event import (
    ResponseCompletedEvent,
)
from byteplussdkarkruntime.types.responses.response_output_item_done_event import (
    ResponseOutputItemDoneEvent,
)
from byteplussdkarkruntime.types.responses.response_function_tool_call import (
    ResponseFunctionToolCall,
)
from byteplussdkarkruntime.types.responses.response_mcp_item import McpApprovalRequest


# Example code: Demonstrating common usages of the Responses API
# -------------------------------------------------
# 1. Using caching in multi-turn conversations
# 2. Calling external functions (function calling)
# 3. Using MCP tools (MCP)


client = AsyncArk(api_key="${YOUR_API_KEY}")
model_or_endpoint_id = "seed-1-6-250615"


async def main():
    # ==========================================================
    # Example 1: Multi-turn conversation with caching enabled
    # ==========================================================
    print("Example 1: Use caching for multi-round chat")
    # ---------- Round 1 ----------
    # Note: Enable caching; store=True means storing the conversation on the server for later reference
    stream = await client.responses.create(
        model=model_or_endpoint_id,
        input=[
            {"role": "system", "content": "you are a helpful assistant"},
            {"role": "user", "content": "hello"},
        ],
        caching={
            "type": "enabled",
        },
        store=True,
        stream=True,
    )
    response_id = ""
    async for event in stream:
        print(event)
        if isinstance(event, ResponseCompletedEvent):
            response_id = event.response.id

    # ---------- Round 2 ----------
    # Note: Link to the previous round’s context using previous_response_id
    print("prev response id", response_id)
    stream = await client.responses.create(
        model=model_or_endpoint_id,
        previous_response_id=response_id,
        input=[
            {"role": "user", "content": "Who are you?"},
        ],
        caching={
            "type": "enabled",
        },
        store=True,
        stream=True,
    )
    async for event in stream:
        print(event)

    # ==========================================================
    # Example 2：Function Calling
    # ==========================================================
    print("Example 2: Use responses API for function calling")

    # ---------- Round 1 ----------
    # Check beijing's weather
    stream = await client.responses.create(
        model=model_or_endpoint_id,
        input=[
            {"role": "user", "content": "How is the weather today in Beijing?"},
        ],
        tools=[
            {
                "type": "function",
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "City name, example Beijing",
                        },
                        "unit": {
                            "type": "string",
                            "description": "temperature unit. example celsius",
                        },
                    },
                    "required": ["location"],
                },
            }
        ],
        caching={
            "type": "enabled",
        },
        store=True,
        stream=True,
    )
    call_id = ""
    response_id = ""
    async for event in stream:
        print(event)
        if isinstance(event, ResponseCompletedEvent):
            response_id = event.response.id
        if isinstance(event, ResponseOutputItemDoneEvent) and isinstance(
            event.item, ResponseFunctionToolCall
        ):
            call_id = event.item.call_id

    # ---------- Round 2 ----------
    # Pass the function call result back to the model, so that it can continue to generate the final answer
    stream = await client.responses.create(
        model=model_or_endpoint_id,
        previous_response_id=response_id,
        input=[
            {
                "type": "function_call_output",
                "call_id": call_id,
                "output": '{"temperature": "30"}',
            },
        ],
        caching={
            "type": "enabled",
        },
        store=True,
        stream=True,
    )
    async for event in stream:
        print(event)

    # ==========================================================
    # Example 3：MCP
    # ==========================================================
    # ---------- Round 1 ----------
    # Check the documentation of this repo
    stream = await client.responses.create(
        model=model_or_endpoint_id,
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "check the repo structure expressjs/express ",
                    }
                ],
            }
        ],
        tools=[
            {
                "type": "mcp",
                "server_label": "deepwiki-test",
                "server_url": "https://mcp.deepwiki.com/mcp",
                "require_approval": "always",
            }
        ],
        store=True,
        stream=True,
    )
    approval_id = ""
    response_id = ""
    async for event in stream:
        print(event)
        if isinstance(event, ResponseCompletedEvent):
            response_id = event.response.id
        if isinstance(event, ResponseOutputItemDoneEvent) and isinstance(
            event.item, McpApprovalRequest
        ):
            approval_id = event.item.id

    # ---------- Round 2 ----------
    # Approve the mcp tool call
    stream = await client.responses.create(
        model=model_or_endpoint_id,
        input=[
            {
                "type": "mcp_approval_response",
                "approval_request_id": approval_id,
                "approve": True,
            }
        ],
        previous_response_id=response_id,
        tools=[
            {
                "type": "mcp",
                "server_label": "deepwiki-test",
                "server_url": "https://mcp.deepwiki.com/mcp",
                "require_approval": "always",
            }
        ],
        store=True,
        stream=True,
    )
    async for event in stream:
        print(event)


if __name__ == "__main__":
    asyncio.run(main())

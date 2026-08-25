"""
The first tool call.
"""

import json
from dotenv import load_dotenv
from openai import OpenAI

MODEL = "gpt-5.6-luna"

load_dotenv()

def get_order_status(order_id: str) -> str:
    """Return the status of an order."""
    return "The order has been shipped and should arrive tomorrow."

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_order_status",
            "description": "Get the current status of an order.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "The order ID.",
                    }
                },
                "required": ["order_id"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    }
]

messages=[{"role": "user", "content": "Where is order A123?"}]

client = OpenAI()
response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    tools=tools,
    reasoning_effort="none"
)

message = response.choices[0].message
print("The content:", message.content)

tool_call = message.tool_calls[0]
print("Request ID:", tool_call.id)
print("Function name:", tool_call.function.name)
print("Arguments:", tool_call.function.arguments)

arguments = json.loads(tool_call.function.arguments)
order_status = get_order_status(**arguments)
print(order_status)

messages.append(message)
messages.append(
    {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": order_status,
    }
)

response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
)

print(f"Final response: {response.choices[0].message.content}")

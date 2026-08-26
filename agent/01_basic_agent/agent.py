"""A minimal, interactive agent loop with one retrieval tool."""

import json
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI

from tool_retrieve import TOOLS, reset_seen_ids, retrieve

MODEL = "gpt-5.6-luna"

SYSTEM_PROMPT = """
You are an assistant answering campus-related questions.

Answer only when all the facts necessary for a complete answer are available. Answer in a concise, clear, and direct manner, without any extra information.

If any necessary information is missing, you MUST call an available tool to search specifically for that missing information. Do not answer using only the supported parts while merely noting that other required information is unavailable.

It is OK to use the same tool more than once.

Once there are at least two tool calls that did not return any relevant information, say "I don't know".
"""

TOOL_MAP = {"retrieve": retrieve}


def call_tool(name: str, arguments: str) -> dict[str, Any]:
    """Run one named tool and turn bad tool calls into useful model feedback."""
    try:
        print(f"Running tool: {name}")
        handler = TOOL_MAP[name]
        result = handler(**json.loads(arguments))
        return result
    except (KeyError, TypeError, json.JSONDecodeError, ValueError) as error:
        print(f"Tool failed: {name}: {error}")
        return {"error": f"Tool call failed: {error}"}


def run_agent(messages: list) -> str:
    """Continue asking the model until it returns a response without tool calls."""
    reset_seen_ids()
    conversation = [{"role": "developer", "content": SYSTEM_PROMPT}, *messages]
    turn = 0
    while True:
        turn += 1
        print(f"\n=== Turn {turn} ===")
        completion = client.chat.completions.create(
            model=MODEL,
            messages=conversation,
            tools=TOOLS,
            reasoning_effort="none",
        )
        assistant_message = completion.choices[0].message
        conversation.append(assistant_message)

        if not assistant_message.tool_calls:
            return assistant_message.content

        for tool_call in assistant_message.tool_calls:
            result = call_tool(tool_call.function.name, tool_call.function.arguments)
            conversation.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result),
                }
            )


if __name__ == "__main__":
    load_dotenv()
    client = OpenAI()
    query = "Where on campus can I study quietly on Friday?"
    # query = "Where on campus do they dance on Friday?"
    messages = [{"role": "user", "content": query}]
    print(f"Answer: {run_agent(messages)}")

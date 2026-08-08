import argparse
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

from call_function import available_functions, call_function
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError("OpenRouter API key not found")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    for _ in range(20) : # call the model, handle responses
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            temperature=0,
            tools=available_functions
        )
        if response.usage is None:
            raise RuntimeError("usage metadata not found")
        if args.verbose:
            print(
                f"User prompt: {args.user_prompt}\n"
                f"Prompt tokens: {response.usage.prompt_tokens}\n"
                f"Response tokens: {response.usage.completion_tokens}"
            )
        message = response.choices[0].message
        messages.append(message)

        if message.tool_calls :
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, args.verbose)
                if (result_message['content'] is None) or (result_message['content'] == "") :
                    raise Exception("result message is empty")
                if args.verbose :
                    print(f"-> {result_message['content']}")
                messages.append(result_message)
        else:
            print(message.content)
            return

        if _ == 19 :
            sys.exit(1)


if __name__ == "__main__":
    main()
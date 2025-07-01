import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():
    load_dotenv()

    # Get command line arguments (excluding script name)
    args = sys.argv[1:]

    # Check for verbose flag
    verbose = False
    if "--verbose" in args:
        verbose = True
        args.remove("--verbose")

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        print('Example: python main.py "How do I build a calculator app?" --verbose')
        sys.exit(1)

    user_prompt = " ".join(args)
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, user_prompt, verbose)


def generate_content(client, messages, user_prompt, verbose=False):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
        )

        print("Response:")
        print(response.text)

        if verbose:
            print(f"User prompt: {user_prompt}")

            # Check if usage metadata is available
            if hasattr(response, "usage_metadata"):
                usage = response.usage_metadata
                print(f"Prompt tokens: {usage.prompt_token_count}")
                print(f"Response tokens: {usage.candidates_token_count}")
            else:
                print("Token usage information not available")

    except Exception as e:
        print(f"Error generating content: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

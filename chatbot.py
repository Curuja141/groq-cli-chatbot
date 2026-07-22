from dotenv import load_dotenv
from groq import Groq
import os
from colorama import Fore, init


# Load environment variables from the .env file
load_dotenv()

# Initialize Colorama
init(autoreset=True)


# Get environment variables
api_key = os.getenv("GROQ_API_KEY")
model_name = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")


# Check whether the API key was found
if not api_key:
    raise ValueError(
        "GROQ_API_KEY was not found. "
        "Create a .env file based on the .env.example file."
    )


# Create the Groq client
client = Groq(api_key=api_key)


def generate_response(messages):
    """
    Sends the conversation history to the Groq API
    and displays the response in real time.
    """

    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0.3,
        max_tokens=1000,
        stream=True,
    )

    print(f"{Fore.CYAN}Assistant: ", end="")

    full_response = ""

    for response_chunk in response:
        text = response_chunk.choices[0].delta.content

        if text:
            print(text, end="", flush=True)
            full_response += text

    print()

    messages.append(
        {
            "role": "assistant",
            "content": full_response,
        }
    )

    return messages


def start_chatbot():
    """
    Starts the chatbot and keeps the conversation running
    until the user types 'exit'.
    """

    print(f"{Fore.GREEN}Welcome to the AI chatbot!")
    print("Type 'exit' to close the application.\n")

    messages = []

    while True:
        user_input = input(f"{Fore.LIGHTYELLOW_EX}You: ").strip()

        if user_input.lower() == "exit":
            print(f"{Fore.GREEN}Chatbot closed.")
            break

        if not user_input:
            print(f"{Fore.RED}Please type a message.")
            continue

        messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        try:
            messages = generate_response(messages)

        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Request interrupted by the user.")

        except Exception as error:
            print(f"{Fore.RED}An error occurred: {error}")


if __name__ == "__main__":
    start_chatbot()
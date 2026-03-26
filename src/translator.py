import os
# Use Ollama library to interact with model:
from ollama import chat, ChatResponse, Client
import subprocess

# process = subprocess.Popen(['ollama', 'serve'])

# Get OLLAMA_HOST, if specified, or default to localhost:11434.
MODEL_NAME = "mistral:7b"
OLLAMA_URL = os.getenv("OLLAMA_HOST", "localhost:11434")

client = Client(host=OLLAMA_URL)


# TODO: Implement Basic LLM integration
def get_language(post: str) -> str:
    context = """You are a language classifier. Detect the language of the input text and reply only with the English name of that language.
              Example:
              INPUT: Bonjour, je m'appelle Bob
              OUTPUT: French

              INPUT: Können Sie mir bitte helfen?
              OUTPUT: German

              INPUT: Hello, how are you?
              OUTPUT: English
              """
    response = client.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": context
            },
            {
                "role": "user",
                "content": post
            }
        ]
    )
    return response.message.content

# TODO: Implement Basic LLM integration
def get_translation(post: str) -> str:
    context = """You are a translator. Translate the input text into English. If the input text is already in english, please return the text as-is
              Reply only with the translated text and nothing else.

              Example:
              INPUT: Bonjour, je m'appelle Bob
              OUTPUT: Hello, my name is Bob

              INPUT: Können Sie mir bitte helfen?
              OUTPUT: Can you please help me?
              """
    response = client.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": context
            },
            {
                "role": "user",
                "content": post
            }
        ]
    )
    return response.message.content.strip()

def translate_content(post: str) -> tuple[bool, str]:
    """
    Calls get_language to detect the post language.
    If English (or unrecognisable), returns (True, original_post).
    Otherwise calls get_translation and returns (False, translated_post).
    Never raises an exception for any textual input.
    """
    detected_language = get_language(post).strip()

    if detected_language.lower() == "english":
        return (True, post)

    translated = get_translation(post)
    return (False, translated)



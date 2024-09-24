import os
from dotenv import load_dotenv
from eval_config import ENV_PATH

def load_env_variables():
    if os.path.exists(ENV_PATH):
        load_dotenv(dotenv_path=ENV_PATH)
        if os.getenv("OPENAI_API_KEY"):
            print("OpenAI API key loaded successfully.")
        else:
            print("OpenAI API key not found in .env file.")
    else:
        print(f".env file not found at {ENV_PATH}")

    # You can add more environment variable checks here if needed

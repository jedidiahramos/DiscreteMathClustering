import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

def get_response(message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system", 
                "content": 
                    "You are a question classifier. Classify the user's input question into one of the following categories: "
                    "'Sets, Proofs, and Induction', "
                    "'Formal Logic', "
                    "'Relations', "
                    "'Functions'. "
                    "Respond with only the category name."
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )
    return response.choices[0].message.content

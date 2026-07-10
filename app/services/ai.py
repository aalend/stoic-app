import json

from flask import current_app
from google.genai import Client


def get_stoic_wisdom(entry_text):
    client = Client(api_key=current_app.config['GEMINI_API_KEY'])

    prompt = f"""
        The user wrote this journal entry: "{entry_text}"

        Analyze the entry and return ONLY a valid JSON object (no markdown, no explanations):
        {{
            "themes": ["theme1", "theme2"],
            "cards": [
                {{
                    "author": "author name",
                    "quote": "quote",
                    "principle": "principle name",
                    "bridge": "how this relates to the user's entry"
                }}
            ]
        }}

        Authors: Marcus Aurelius, Epictetus, Seneca.
        Return 2-3 themes and 3 cards.
        """

    response = client.models.generate_content(
        model='gemini-3.1-flash-lite', contents=prompt
    )

    raw = response.text.strip()
    clean = raw.replace('```json', '').replace('```', '').strip()

    return json.loads(clean)

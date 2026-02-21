import os

from openai import OpenAI


class Agent:
    def __init__(self):
        api_key = os.environ.get("DEEPSEEK_API_TOKEN")
        if not api_key:
            raise ValueError("DEEPSEEK_API_TOKEN environment variable is required")

        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        self.model = "deepseek-chat"

    def process_request(self, text: str):
        try:
            cleaned_text = self._clean_input(text)

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": cleaned_text},
                ],
                max_tokens=500,
                temperature=0.7,
            )

            if response.choices and response.choices[0].message:
                return response.choices[0].message.content
            else:
                return "I received your message but couldn't generate a response."

        except Exception as e:
            return f"Error processing request: {str(e)}"

    def _clean_input(self, text: str) -> str:
        import re

        text = re.sub(r"<@[A-Z0-9]+>", "", text)
        return text.strip()

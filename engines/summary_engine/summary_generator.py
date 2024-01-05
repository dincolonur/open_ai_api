import openai
from models.ConfigModel import ConfigModel


class SummaryGenerator:

    @staticmethod
    def generate_summary():
        openai.api_key = ConfigModel.constants['api_key']
        text = input("Enter any text here: ")
        text = text.replace('\n', ' ')

        tldr_tag = "\n tl;dr:"
        max_tokens = 100
        engine = 'text-davinci-003'

        text = text + tldr_tag
        response = openai.Completion.create(engine=engine,
            prompt=text,
            temperature=0.3,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n\n"]
            )

        print("Text length:", len(text), "\t Response length:", len(response["choices"][0]["text"]) )
        print("Text:\n", text)
        print("="*30, "SUMMARY", "="*30)
        print(response["choices"][0]["text"])

import openai
from models.ConfigModel import ConfigModel


class CodeGenerator:

    @staticmethod
    def generate_code():
        openai.api_key = ConfigModel.constants['api_key']
        prefix = "Input:\nPython code for "
        suffix = "\nOutput:\n"
        engine = 'text-davinci-003'
        max_tok = 3000

        text = "largest merge of two strings"
        text = prefix + text + suffix
        response = openai.Completion.create(engine=engine,prompt=text,
                                                  temperature=0.7,
                                                  max_tokens=max_tok,
                                                  top_p=1,
                                                  frequency_penalty=0,
                                                  presence_penalty=0,
                                                  stop=["Explanation"]
                                                  )
        print(response["choices"][0]["text"])

        # text = "sum of unique elements"
        # text = prefix + text + suffix
        # response = openai.Completion.create(engine=engine,prompt=text,
        #                                           temperature=0.7,
        #                                           max_tokens=max_tok,
        #                                           top_p=1,
        #                                           frequency_penalty=0,
        #                                           presence_penalty=0,
        #                                           stop=["Explanation"]
        #                                           )
        # print(response["choices"][0]["text"])

        # text = "longest palindrome"
        # text = prefix + text + suffix
        # response = openai.Completion.create(engine=engine,prompt=text,
        #                                           temperature=0.7,
        #                                           max_tokens=max_tok,
        #                                           top_p=1,
        #                                           frequency_penalty=0,
        #                                           presence_penalty=0,
        #                                           stop=["Explanation"]
        #                                           )
        # print(response["choices"][0]["text"])

        # text = "convert sorted list to binary search tree"
        # text = prefix + text + suffix
        # response = openai.Completion.create(engine=engine,prompt=text,
        #                                           temperature=0.7,
        #                                           max_tokens=max_tok,
        #                                           top_p=1,
        #                                           frequency_penalty=0,
        #                                           presence_penalty=0,
        #                                           stop=["Explanation"]
        #                                           )
        # print(response["choices"][0]["text"])

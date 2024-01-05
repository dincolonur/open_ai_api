import openai
from models.ConfigModel import ConfigModel


class EmailGenerator:

    @staticmethod
    def generate_email():
        openai.api_key = ConfigModel.constants['api_key']
        iPrefix = "\n\nReview:\n"
        iSuffix = "\n"
        oPrefix = "\nEmail:\n"

        review1 = ConfigModel.constants['review1']
        email1 = ConfigModel.constants['email1']
        review2 = ConfigModel.constants['review2']
        email2 = ConfigModel.constants['email2']
        review3 = ConfigModel.constants['review3']
        email3 = ConfigModel.constants['email3']
        # review1 = "Nice socks, great colors, just enough support for wearing with a good pair of sneakers."
        # email1 = "Dear Customer, Thank you for buying socks form our store. Our socks come in a wide range of colors and types. We also sell sneakers on our platform, make sure to check out the huge collection online. Regards, Time Store"
        # review2 = "Love Deborah Harness's Trilogy! Didn't want the story to end and hope they turn this trilogy into a movie. I would love it if she wrote more books to continue this story!!!"
        # email2 = "Dear Customer, Thank you for purchasing the book from our store. We have many other books from Deborah Harness. We also have many movies with a similar theme. Make sure to check them out! Regards, Time Store"
        # review3 = "SO much quieter than other compressors. VERY quick as well. You will not regret this purchase."
        # email3 = "Dear Customer, Thank you for buying from our platform. Our compressors are among the best in the market. Make sure to check out our wide range of products. Regards, Time Store"

        flow = iPrefix + review1 + iSuffix + oPrefix + email1 + iPrefix + review2 + iSuffix + oPrefix + email2 + iPrefix + review3 + iSuffix + oPrefix


        engine = 'text-davinci-003'
        max_tok = 3000

        review = "Shirt a bit too long, with heavy hem, which inhibits turning over. I cut off the bottom two inches all around, and am now somewhat comfortable. Overall, material is a bit too heavy for my liking."
        text = flow + iPrefix + review + iSuffix + oPrefix
        response = openai.Completion.create(engine=engine,prompt=text,
                                                temperature=0.7,
                                                max_tokens=max_tok,
                                                top_p=1,
                                                frequency_penalty=0,
                                                presence_penalty=0,
                                                stop=["Time Store"]
                                                )
        print(response["choices"][0]["text"])

        # review = "The quality on these speakers is insanely good and doesn't sound muddy when adjusting bass. Very happy with these."
        # text = flow + iPrefix + review + iSuffix + oPrefix
        # response = openai.Completion.create(engine=engine,prompt=text,
        #                                           temperature=0.7,
        #                                           max_tokens=max_tok,
        #                                           top_p=1,
        #                                           frequency_penalty=0,
        #                                           presence_penalty=0,
        #                                           stop=["Time Store"]
        #                                           )
        # print(response["choices"][0]["text"])
        #
        # review = "Beautiful watch face. The band looks nice all around. The links do make that squeaky cheapo noise when you swing it back and forth on your wrist which can be embarrassing in front of watch enthusiasts. However, to the naked eye from afar, you can't tell the links are cheap or folded because it is well polished and brushed and the folds are pretty tight for the most part. love the new member of my collection and it looks great. I've had it for about a week and so far it has kept good time despite day 1 which is typical of a new mechanical watch."
        # text = flow + iPrefix + review + iSuffix + oPrefix
        # response = openai.Completion.create(engine=engine,prompt=text,
        #                                           temperature=0.7,
        #                                           max_tokens=max_tok,
        #                                           top_p=1,
        #                                           frequency_penalty=0,
        #                                           presence_penalty=0,
        #                                           stop=["Time Store"]
        #                                           )
        # print(response["choices"][0]["text"])

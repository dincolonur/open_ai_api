import openai
import pathlib
import io
from PIL import Image
from base64 import b64decode
from models.ConfigModel import ConfigModel


class ImageGenerator:

    @staticmethod
    def generate_image():
        openai.api_key = ConfigModel.constants['api_key']

        # prompt = "A Persian cat in 90s Japanese manga style"
        prompt = "Cat is driving a red car in the river"
        data_dir = pathlib.Path.cwd() / "responses"

        data_dir.mkdir(exist_ok=True)

        response = openai.Image.create(
            prompt=prompt,
            n=3,
            size="256x256",
            response_format="b64_json",
        )

        for item in response["data"]:
            image_data = item["b64_json"]
            image_decoded = b64decode(image_data)
            img = Image.open(io.BytesIO(image_decoded))
            img.show()

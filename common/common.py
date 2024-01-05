import openai
import math

import wget
import yaml
from models.ConfigModel import ConfigModel
from engines.email_engine.email_generator import EmailGenerator
from engines.code_engine.code_generator import CodeGenerator
from engines.summary_engine.summary_generator import SummaryGenerator
from engines.image_engine.image_generator import ImageGenerator

def load_config(yaml_file):

    with open(yaml_file, 'r') as file:
        cfg_service = yaml.safe_load(file)

    input_dict = dict()
    input_dict['api_key'] = cfg_service['api_params']['api_key']

    input_dict['review1'] = cfg_service['email_data']['review1']
    input_dict['email1'] = cfg_service['email_data']['email1']
    input_dict['review2'] = cfg_service['email_data']['review2']
    input_dict['email2'] = cfg_service['email_data']['email2']
    input_dict['review3'] = cfg_service['email_data']['review3']
    input_dict['email3'] = cfg_service['email_data']['email3']

    ConfigModel(input_dict)


def call_email_generator():
    EmailGenerator.generate_email()


def call_code_generator():
    CodeGenerator.generate_code()


def call_summary_generator():
    SummaryGenerator.generate_summary()

def call_image_generator():
    ImageGenerator.generate_image()

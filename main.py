from common import common

if __name__ == "__main__":
    common.load_config('config/config.yaml')
    print('Open AI API starts...')
    # common.call_email_generator()
    # common.call_code_generator()
    # common.call_summary_generator()
    common.call_image_generator()

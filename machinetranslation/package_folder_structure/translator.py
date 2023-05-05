import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

class autho:
    authenticator = IAMAuthenticator('vmzQg_eDZMQGgpw1HeDtG1QK6dZKeSVvT6-828gifDJA')
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator)
    
    language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/d383e43f-bde9-4238-b30c-a74b451c1ad5')
    languages = language_translator.list_languages().get_result()

class Trans_English_To_French:
    def __init__(self, user_text) -> str:
        self.user_text = user_text
    
    def convert_EN_FR(self):
        self.translation = autho.language_translator.translate(self.user_text, model_id='en-fr').get_result()
        return self.translation['translations'][0]['translation']

    
class Trans_French_To_English:
    def __init__(self, user_text) -> str:
        self.user_text = user_text
    
    def convert_FR_EN(self):
        self.translation = autho.language_translator.translate(self.user_text, model_id='fr-en').get_result()
        return self.translation['translations'][0]['translation']
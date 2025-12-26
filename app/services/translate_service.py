import os
import json
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account

# Load JSON from environment variable
credentials_info = json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"])

# Create credentials object
credentials = service_account.Credentials.from_service_account_info(credentials_info)

# Initialize Google Translate client
translator = translate.Client(credentials=credentials)

def translate(word, target_language):
    translation = translator.translate(word, target_language=target_language)
    return translation['translatedText']

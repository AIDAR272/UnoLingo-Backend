import os
from dotenv import load_dotenv
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account

load_dotenv()

# Path to your JSON key
key_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Load credentials
credentials = service_account.Credentials.from_service_account_file(key_path)

# Initialize client with credentials
translator = translate.Client(credentials=credentials)

def translate(word, target_language):
    translation = translator.translate(word, target_language=target_language)
    return translation['translatedText']


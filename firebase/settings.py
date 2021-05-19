from firebase_admin import credentials, initialize_app
from dotenv import load_dotenv
from django.conf import settings
import os

load_dotenv()

cred = credentials.Certificate(
    f"{settings.BASE_DIR}{os.getenv('GOOGLE_APPLICATION_CREDENTIALS')}"
)
virtual_day_app = initialize_app(cred)

import firebase_admin
from firebase_admin import credentials
import os
from dotenv import load_dotenv

load_dotenv()

cred = credentials.Certificate(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
virtual_day_app = firebase_admin.initialize_app(cred)

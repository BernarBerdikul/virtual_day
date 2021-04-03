from firebase_admin import credentials, initialize_app
from virtual_day.utils import constants

cred = credentials.Certificate(constants.GOOGLE_APPLICATION_CREDENTIALS)
virtual_day_app = initialize_app(cred)

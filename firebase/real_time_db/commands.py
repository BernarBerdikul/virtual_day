from firebase_admin import db
from firebase.settings import virtual_day_app

url = "https://virtual-day-default-rtdb.firebaseio.com/"

firebase_config = {
    "apiKey": "AIzaSyBg529_cFeU-yhyFUQA-AwtC-JgpOpe0Y8",
    "authDomain": "virtual-day.firebaseapp.com",
    "databaseURL": "https://virtual-day-default-rtdb.firebaseio.com",
    "projectId": "virtual-day",
    "storageBucket": "virtual-day.appspot.com",
    "messagingSenderId": "433262070988",
    "appId": "1:433262070988:web:480a875708d15f9d754669",
    "measurementId": "G-SQWKWCN8XS"
}

database = db.reference(app=virtual_day_app, url=url)

# push data
data = {"name": "Bernar", "age": 20, "coordinates": {"x": 1, "y": 2, "z": 3}}
database.push(data)

# create own key
data = {"age": 20, "coordinates": {"x": 1, "y": 2, "z": 3}}
database.child("Bernar").set(data)

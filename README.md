# Application "Virtual Day" by Nadir, Bernar and Slava

![menushka icon](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/The_Rim_Fire_in_the_Stanislaus_National_Forest_near_in_California_began_on_Aug._17%2C_2013-0004.jpg/1200px-The_Rim_Fire_in_the_Stanislaus_National_Forest_near_in_California_began_on_Aug._17%2C_2013-0004.jpg "Орк")


**To start project require use versions:**
* python 3.7+
* Django 3+
* Django Rest Framework 3+

**Primarily you need create virtual environment and run it:**
* for Windows
```
python -m venv env
. /env/Scripts/activate
```
* for Linux
```
python3 -m venv env
. /env/bin/activate
```

*if tou use Linux after 'python' and 'pip' add version number, example python3 or pip3*

**In secondary, clone repository from github:** 
```
git clone https://github.com/BernarBerdikul/DRF_template.git
```

**Change your directory in just cloned project and install project libraries in virtual environment:**
```
cd menushka
pip install -r requirements.txt
```

**Then, copy file .env.example and call it like .env. It's will be our environment's variables:**
```
cp .env.example .env
```

**Finally, create models in postgres database and run test server:**
```
python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable
python manage.py runserver
```

**Also you can immediately create super user with all permissions for project:**
```
py manage.py createsuperuser
```

**Trough this link, you can login in project's [admin page](http://127.0.0.1:8000/ru/super_secret_admin/)**

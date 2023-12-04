Please Ensure that your environment include

-pip install django
-pip install djangorestframework
-pip install djangorestframework-xml
-pip install pymysql or mysqlclient
-setting Password/ database for your mysql db

Also, Run migration
-python manage.py makemigrations
-python manage.py migrate

Test
-python manage.py createsuperuser 
-python manage.py runserver
-python manage.py test

Test Path
Viewing Index
http://127.0.0.1:8000/restaurant/
Create users
http://127.0.0.1:8000/auth/users/
Login Token
http://127.0.0.1:8000/auth/token/login
Create Booking
http://127.0.0.1:8000/restaurant/booking/
Create Menu
http://127.0.0.1:8000/restaurant/menu/
Update Check Menu by Id
http://127.0.0.1:8000/restaurant/menu/1 or id


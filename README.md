# poke-project-backend

## Steps to run this program:
1. Git clone
2. cd poke-project-backend
3. Set up virtual enviroment 
```
pipenv shell
```
4. Install dependencies
```
 pip install django djangorestframework django-cors-headers djangorestframework-simplejwt djoser
```
5. Make migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```
6. Run Server
```
python manage.py runserver
```
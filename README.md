# News
If you want to run this project locally follow below steps.
1. First of all, you have to run python3 -m venv venv - to install virtualenv in your pyoject directory. 
2. Then download everything in requirements.txt by running command pip3 install -r requirements.txt or  pip install -r requirements.txt (Python 2).
3. We have two docker-compose files one is to run local and the other for deployment. So go to _development folder and run docker-compose.yml. Then cd .. and ./manage.py runserver to run our project. 
4. We have basic CRUD API, but to Put, Delete and Patch methods you have to authenticate. For this we have register/ and login/ endpoints. First register {"username": " ", "password": " ", "email": " " } like this in Json format. Fill in blank spaces. Then login by Username and Password, I am sending back only token and it contains username, email and user id.
5. Copy Token and keep it, you will need it. 

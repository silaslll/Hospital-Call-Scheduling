# Hospital-Call-Scheduling


1 Clone repo into local

In the terminal type:

git clone https://github.com/silaslll/Hospital-Call-Scheduling.git


2 Migrate database

In the terminal type:

python manage.py makemigrations

and:

python manage.py migrate


3 Run the server by typing:

python manage.py runserver  


4 In the browser, test the follwing url:

To create new info:
http://localhost:8000/docinfos/new

To view all infos:
http://localhost:8000/docinfos

To access admin page:
http://localhost:8000/admin/

admin user name: admin  / password: admin

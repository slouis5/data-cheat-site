# data-cheat-site
Data Cheat Site is a Platform where beginner in the Data World can learn and practice basics about statistics at the level they want.

## To test on your own

### Requirements
 <!-- Linux OS (if you don't have it, install it; if you can't use it, raise your skills)-->
 - Python 3.10 or higher (pre-installed on most Linux distributions)
 - Postgresql 12 or higher (you can use another RDBMS but you will need to configure the settings.py file accordingly, see [here](https://docs.djangoproject.com/en/5.1/topics/install), **Get your database running** section).

### Instructions

1. **Clone the repo**  
Go to the directory where you want to clone the repo, open the terminal on it and **Clone the project** using Git:  
~~~bash  
    git clone https://github.com/slouis5/sql-cheat-site.git
~~~

2. **Cerate a virtual environement**  
Go to the project directory
~~~bash  
    cd sql-cheat-site
~~~
Create a virtual environment:
~~~bash   
# macOS/Linux
# You may need to run `sudo apt-get install python3-venv` first on Debian-based OSs
python3 -m venv .venv

# Windows
python -m venv .venv
# Note .venv is the python virtual environnement name
~~~

Activate your virtual environment
~~~bash
# Mac/linux 
source .venv/bin/activate

# Windows
.venv\Scripts\activate.bat
~~~

3. **Install the Requirements**  
Install the python packages with:

~~~bash  
  pip install -r requirements.txt
~~~
_(don't forget to install additional package if you are not using Postgres as RDBMS)_

4. **Create a Postgres Database for the project and a user for it**
Note those details for the next step:
- DB_NAME: The name of the database
- USER_NAME: The username
- PASSWORD: The password for the user created

5. **Create an environement file**  
create a .env file in the same directory of your settings.py file and configure those variables:
~~~bash
DEBUG = "True"
DB_NAME  = "<bd_name>"
DB_USER = "<user_name>"
DB_PASSWORD = "***********"
DB_HOST = "localhost"
PORT = "5432"
SECRET_KEY = "************************************************************"
~~~

_(to generate a secret key, you can open a python terminal and type those comand lines below):_
~~~bash

python

>>> from django.core.management import utils
>>> print(utils.get_random_secret_key())
~~~
Don't forget to fill the SECRET_KEY value in the .env file you created by the generated SECRET_KEY.

6. **Apply migrations and migrate**  
6.1. Modify the ENGINE value in the settings.py file accordingly to the RDBMS you are using if it's not Postgres ([See here](https://docs.djangoproject.com/en/5.1/ref/settings/) in ENGINE section).  
6.2 From the terminal, navigate to the data_cheat_site folder containing the settings.py file and run the following lines:
~~~bash
# creating tables in the database from models

# generate SQL Commands
python manage.py makemigrations

# Excecute SQL Commands
python manage.py migrate
~~~

7. **Create a Administrator for the site**  
Run this to create your admin user:
~~~bash
  python manage.py createsuperuser
~~~

8. **Launch the app**  
Go to the directory containing the manage.py file, and run this:
~~~bash
  python3 manange.py runserver
~~~

_(If you are on Linux and you got peer authetification failed message for your DB_USER,_)  
use:
~~~bash
  sudo nano pg_hba.conf
~~~
_at `etc/postgresql/[version]/main/` to change *peer* methode for local to *md5* in your pg_hba.conf file_  
_Then restart the service via `sudo systemctl restart postgresql`_.

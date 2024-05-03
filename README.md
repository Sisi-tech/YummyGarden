## Project Name: SCoffee
## Django

## Learned and Practiced 

## Templates
**Set up**

- [x] **Add 'templates' to 'DIRS' on the settings.py file**
      
## Example:

```Python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
- [x] **Create templates folder under the app folder**
- [x] **Create different html file. Such as about.html, home.html, menu.html**
- [x] **Write function and render the request and HTML file**
- [x] **Can add style to the HTML file**

## Connect to Database - MySQL
**Set up**
- [x] **Install mysqlclient: pip install pymysql mysqlclient**
- [x] **Add the following code under app section __init__.py**
```Python
import pymysql

pymysql.install_as_MySQLdb()
```
- [x] **Create mysql.py under app section and add the following format to it**
```Python
import mysql.connector as connector

connection = connector.connect(user='root', password='')

cursor = connection.cursor()
cursor.execute("CREATE DATABASE MenuSales")
cursor.execute("USE MenuSales")

connection.close()
```
- [x] **Add the following to the settings.py file**
```Python
      DATABASES = {
		'default': {
				'ENGINE': 'django.db.backends.mysql',
				'NAME': 'databasename',
				'HOST': '127.0.0.1',
				'PORT': '3306',
				'USER': 'admindjango',
				'PASSWORD': 'password',
		}
}
```
- [x] **Run python manage.py makemigrations**
- [x] **Run python manage.py migrate**

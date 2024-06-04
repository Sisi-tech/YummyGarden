## Project Name: Yummy Garden
## Django

## Video walk through
<div>
    <a href="https://www.loom.com/share/25226b2614b74d2fab90c2f9c9ec496b">
      <p>Yummy Garden - 3 June 2024 - Watch Video</p>
    </a>
    <a href="https://www.loom.com/share/25226b2614b74d2fab90c2f9c9ec496b">
      <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/25226b2614b74d2fab90c2f9c9ec496b-with-play.gif">
    </a>
</div>

## env
**source venv/bin/activate**

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

## License

    Copyright [2024] [Sisi Wang]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

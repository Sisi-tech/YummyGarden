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

**Connect to Database - MySQL**
**Set up**

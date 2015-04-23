SECRET_KEY = ' '

INSTALLED_APPS = (
    'file',
    'app_one',
    'app_two',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

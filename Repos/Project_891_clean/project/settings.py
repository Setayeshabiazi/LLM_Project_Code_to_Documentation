   

from pathlib import Path

                                                                
BASE_DIR = Path(__file__).resolve().parent.parent


                                                              
                                                                       

                                                                  
SECRET_KEY = 'django-insecure-=_t70q*sb@8kjbnm3^v=6=#68k-u6fsytd0#%%w&5n*u0xny#3'

                                                                 
DEBUG = True

ALLOWED_HOSTS = []


                        

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'project_app.apps.ProjectAppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'project.wsgi.application'


          
                                                               

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


                     
                                                                              

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


                
                                                          
AUTH_USER_MODEL = 'project_app.User'
AUTH_EMAIL_DOMAIN = '@uwm.edu'

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/courses/'
LOGOUT_REDIRECT_URL = '/login/'


                      
                                                    

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


                                        
                                                           

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]


                                
                                                                        

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

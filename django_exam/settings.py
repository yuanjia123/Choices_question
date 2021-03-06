

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ')l7&&)86r)t(^bgtbyhhydf(-r$e+6-me)3j&1#m+@)!o54)b#'


DEBUG = True

# ALLOWED_HOSTS = [ '192.168.56.1']
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'exam_test.apps.ExamTestConfig',
    'users.apps.UsersConfig',
    'newuser.apps.NewuserConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_exam.urls'

# 文件上传配置  (写入文件)  所有上传的文件都在media下面   (指定文件上传的相对路径media/imgs/)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

#访问文件的目录 （读取文件） 所有要访问的文件都在这下面
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #给每一个页面传递一个media_url这样的变量
                #这个是类似于flask上下文处理器的东西(把media的路径传递到每个模板 )  按住ctrl点击 'django.template.context_processors.media'的media里面会返回一个settings.MEDIA_URL
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'django_exam.wsgi.application'

#继承django自带的用户类  第二步
AUTH_USER_MODEL = "users.UserProfile"
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# 数据库连接信息
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "stu1",
        "USER":"root",
        "PASSWORD":"123456",
        "HOST":"127.0.0.1"
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

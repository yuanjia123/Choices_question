from exam_test import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert/', views.index),
    path('question/<name>/', views.question_choice,name='question'),
    path('test/', views.test,name='test'),
    path('upload/', views.upload,name='upload'),
    path('score/<random_li>/<name>/', views.score,name ='score' ),
    path('', include('users.urls')),
    path('weather/', views.location_weather,name='location_weather'),
    path('weaher_data_json/', views.location_weather,name='location_weather'),
    # path('', include('newuser.urls')),
]

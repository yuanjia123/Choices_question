from exam_test import views
from django.contrib import admin
from django.urls import path,include
from exam_test.views import Weather_View
urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert/', views.index),
    path('question/<name>/', views.question_choice,name='question'),
    path('test/', views.test,name='test'),
    path('upload/', views.upload,name='upload'),
    path('score/<random_li>/<name>/', views.score,name ='score' ),
    path('', include('users.urls')),
    path('weather/', views.location_weather,name='location_weather'),
    path('weaher_data_json/', Weather_View.as_view(),name='weather_View'),
    # path('', include('newuser.urls')),
]

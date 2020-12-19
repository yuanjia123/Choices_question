from exam_test import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert/', views.index),
    path('question/<name>/', views.question_choice,name='question'),
    path('test/', views.test,name='test'),
    path('score/<random_li>/<name>/', views.score,name ='score' ),
    path('user/', include('users.urls')),
    path('', include('newuser.urls')),
]

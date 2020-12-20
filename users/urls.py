from django.urls import include, path
from users import views


urlpatterns = [
    # path('/login/', Login.as_view(), name='Login'),
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),

]
from django.urls import include, path
from users import views


urlpatterns = [
    # path('/login/', Login.as_view(), name='Login'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),

]
from django.urls import include, path
from users import views


urlpatterns = [
    # path('/login/', Login.as_view(), name='Login'),
    path('login/', views.login, name='login'),

]
from django.urls import include, path
from users import views


urlpatterns = [
    # path('/login/', Login.as_view(), name='Login'),
    path('register/', views.register, name='register'),
    path('upload_img/', views.upload_img, name='upload_img'),
    path('', views.login, name='login'),

]
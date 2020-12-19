from django.urls import include, path
from newuser import views


urlpatterns = [
    # path('/login/', Login.as_view(), name='Login'),
    path('newfirst/', views.toAddNew, name='newfirst'),
    path('checkuid/', views.doCheckUid, name='checkuid'),

    path('getpng/', views.createImg),
    path('checkcode/', views.returnCheckCode),
    path('addnew/', views.doAddNew),

]
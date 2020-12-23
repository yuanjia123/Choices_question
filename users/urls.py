from django.urls import include,path
from django.conf.urls import url
from users import views
#关于静态文件图片的访问
from django.views.static import serve
from django_exam.settings import MEDIA_ROOT
urlpatterns = [
    # path('/login/', Login.as_view(), name='Login'),
    path('register/', views.register, name='register'),
    path('upload_img/', views.upload_img, name='upload_img'),
    path('showall_img/', views.showall_img, name='showall_img'),
    path('login/', views.Login_View, name='login'),
    path('', views.Main_View, name='main'),

    # 1、为了整理、上传的图片、我们把所有的上传文件放到media文件夹下面、并且为它创建url访问地址   在setting当中设置两行 151行 152行
    # 2、设置了setting之后、依然是一个破图、显示不了
    # 3、配置关于media中图片的访问
    # 4、r'^media/(?P<path>.*)$' 的意思是取出media文件夹后面的文件把他放到path这个路径当中,
    # 5、server 静态文件的访问url 地址， 这个地址是key:value的形式存储在 Media_root路径下面
    #上传到服务器的照片、进行显示img的src属性、也需要配置路由、这个就是他的路由
    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),

]
from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('homepage/', homepage, name='homepage'),
    path('logout/', logout_user, name='logout'),
    path('category/<slug:category_id>',get_categorys,name='category')# прилетаем с homepage.html,отправляем <int:category_id> в views get_categorys
]

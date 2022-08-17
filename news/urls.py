from django.urls import path

from news.views import home, get_category, register, user_logout, user_login, detail

urlpatterns = [
    path('',home,name='home'),
    path('category/<int:category_id>/',get_category, name='category'),
    path('detail/<int:new_id>/',detail, name='detail'),
    path('register/',register,name='register'),
    path('logout/',user_logout,name='logout'),
    path('login/',user_login,name='login'),
]
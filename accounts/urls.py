from django.urls import path
from . import views
app_name = 'auth'
#configure accnouts urls

urlpatterns = [

    path('auth/login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('auth/logout/', views.user_logout, name='logout'),

]
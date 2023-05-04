from django.urls import path
from firstapp.views import index, user_login
from django.contrib.auth import views as django_views
app_name = 'firstapp'

urlpatterns = [
    path('' , index, name='index'),
    path(
        'login/',
        user_login,
        name='login',
    ),

]
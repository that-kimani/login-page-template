from django.urls import path
from . import views

urlpatterns = [
    path('' , views.login_page , name='home'),
    path('login/' , views.login_page, name='login_page'),
    path('authenticate/' , views.user_authenticate , name='user_authenticate'),
    path('dashboard/' , views.dashboard , name='dashboard'),
    path('signup/' , views.signup , name='signup'),
    path('createuser/' , views.create_user , name='create_user'),
]
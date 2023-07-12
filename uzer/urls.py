from django.urls import path
from .views import registration_views, login_views,logout_views

app_name = 'user'
urlpatterns = [
    path('registration/', registration_views, name='registration'),
    path('login/', login_views, name='login'),
    path('logout/', logout_views, name='logout'),
]

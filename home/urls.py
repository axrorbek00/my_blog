from .views import my_home_view, creat_post_view, post_detail_views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path("", my_home_view, name='my_home'),
    path("create_post/", creat_post_view, name='create_post'),
    path('detail/<int:id>/', post_detail_views, name='detail')
]

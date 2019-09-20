from django.urls import path
from . import views

urlpatterns = [
    path('all_posts/',views.all_post, name='all_posts'),
    path('insert_post/',views.insert_post, name='insert_post'),
    path('update_post/',views.update_post, name='update_post'),
    path('delete_post/',views.delete_post, name='delete_post'),
]
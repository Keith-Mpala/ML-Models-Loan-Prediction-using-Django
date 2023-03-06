from django.urls import path
from . import views

app_name = "authentication"  #

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('sign_up', views.sign_up, name="sign_up"),
    path('create-comment',views.create_comment, name="create_comment"),
    path('reviews', views.reviews, name="reviews"),
    path('create_ML1', views.create_ML1, name='create_ML1'),
    path('create_ML2', views.create_ML2, name="create_ML2"),
]

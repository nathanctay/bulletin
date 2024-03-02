from . import views
from django.urls import path

app_name='bulletin'
urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('registerUser', views.registerUser, name="registerUser"),
    path('login', views.login, name="login"),
    path('<str:id>', views.post, name="post"),
    path('<str:id>/comment', views.comment, name="comment")
]
from . import views
from django.urls import path, include

app_name='bulletin'
urlpatterns = [
    path('', views.index, name="index"),
    
    path('register', views.register, name="register"),
    path('registerUser', views.registerUser, name="registerUser"),
    path('login', views.login, name="login"),
    path('loginUser', views.loginUser, name="loginUser"),
    path('bulletin/<str:id>', views.bulletin, name="bulletin"),
    path('bulletin-edit/', views.bulletinEdit, name="bulletin-new"),
    path('bulletin-edit/<str:bulletinId>', views.bulletinEdit, name="bulletin-edit"),
    path('post-edit/<str:bulletinId>', views.postEdit, name="post-new"),
    path('post-edit/<str:bulletinId>/<str:postId>', views.postEdit, name="post-edit"),
    path('explore/<int:distance>', views.explore, name="explore"),
    path('<str:id>', views.post, name="post"),
    path('<str:id>/comment', views.comment, name="comment"),

]
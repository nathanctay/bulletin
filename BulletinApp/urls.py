from . import views
from django.urls import path

app_name='bulletin'
urlpatterns = [
    path('', views.index, name="index"),
    path('<str:id>', views.post, name="post"),

]
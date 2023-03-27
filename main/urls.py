from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns=[
    path('',Index),
    path('about/',About),
    path('comment/',Comment),
    path('comment_send/',Send_msg),
    path('blogdetail/<int:pk>',BlogDetail.as_view()),
    path('post_com/',Post_Com),
    path('contact/',Contact) ,
    path('message/',Send_msg),
    path('practise/',Practise),
    path('news/',New),
    

]
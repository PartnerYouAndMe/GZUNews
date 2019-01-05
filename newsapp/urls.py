from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list,name='Home'),
    # http://localhost:8000/1
    path('<int:news_pk>',views.news_detail,name='news_detail'),
    path('news_list/',views.news_list),
    path('introduct/',views.introduct,name='my_introduct')
]
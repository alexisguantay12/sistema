from django.urls import path 
from libreria import views
urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('documento',views.documento,name='documento'),
    path('multimedia',views.multimedia,name='multimedia'),
]
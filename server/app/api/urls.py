from django.urls import path
from .views import *


# create your urls here

urlpatterns = [
    path('allmusictracks/',getallmusic.as_view(),name='allmusic'),
    path('postmusic/',uploadmusic.as_view(), name='uploadmusic'),
    path('music/<int:id>',delivermusic.as_view(),name="getmusicbyid")
]

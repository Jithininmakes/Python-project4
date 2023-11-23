from.import views
from django.urls import path

import taskapp

urlpatterns = [
    path('',views.voice,name='voice')



]

from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('table/', Table),
    path('api', api_post_sensor)

]

# -*- coding: utf-8 -*-
from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register(r'taskgroups', views.TaskGroupViewSet, basename='taskgroup')

app_name = 'hueydrfapi'
urlpatterns = router.urls

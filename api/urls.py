from django.conf.urls import url,include
from rest_framework import routers
from api import views as viewset

router = routers.DefaultRouter()

router.register(r"users",viewset.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]


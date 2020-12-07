from django.conf.urls import url,include
from rest_framework import routers
from api import views as viewset
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = routers.DefaultRouter()

router.register(r"users",viewset.UserViewSet)

urlpatterns = [
    url(r"token/",TokenObtainPairView.as_view(),name = "token_obtain_pair"),
    url(r"token/refresh/",TokenRefreshView.as_view(),name = "token_obtain_pair"),
    url(r'^', include(router.urls)),
]


from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)
from rest_framework.routers import DefaultRouter
from authentication.views import RegisterView, ProfileViewSet, CustomerViewSet

router = DefaultRouter()
router.register(r"customers", CustomerViewSet, basename="customer")
router.register(r"profiles", ProfileViewSet, basename="profile")


urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="auth_register"),
]

urlpatterns += [
    path("", include(router.urls)),
]

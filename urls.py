from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from orders.views import OrderViewSet, DriverOrderViewSet
from users.views import UserViewSet, DriverInfoViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'driver-orders', DriverOrderViewSet, basename='driver-order')
router.register(r'users', UserViewSet)
router.register(r'drivers', DriverInfoViewSet, basename='driver-info')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', include('users.urls')),
    path('api/drivers/', include('users.urls')),
] 
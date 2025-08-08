from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, UserViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework import routers
from userapi.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    #other paths
    path(r'', include(router.urls)),
]
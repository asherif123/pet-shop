from rest_framework.routers import DefaultRouter
from pets import views


class OptionalSlashRouter(DefaultRouter):
    """Just to change the default behavior of trailing slashes so
    that urls can now work with or without trailing slashes."""
    def __init__(self, *args, **kwargs):
        super(DefaultRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = '/?'


router = OptionalSlashRouter()
router.register(r'pets', views.PetViewSet)
router.register(r'orders', views.OrderViewSet)
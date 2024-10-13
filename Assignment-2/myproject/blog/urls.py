from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TagViewSet, AuthorViewSet, PostViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"tags", TagViewSet)
router.register(r"authors", AuthorViewSet)
router.register(r"posts", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

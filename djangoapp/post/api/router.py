from rest_framework.routers import DefaultRouter
from post.api.views import PostApiViewSet


router_post = DefaultRouter()
router_post.register(prefix='post', viewset=PostApiViewSet, basename='post')
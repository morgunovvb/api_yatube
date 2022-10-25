from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet


v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
v1_router.register('groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('v1/', include(v1_router.urls)),
]

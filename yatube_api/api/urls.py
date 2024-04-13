from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from django.urls import path

from api.views import CommentViewSet, GroupViewSet, PostViewSet

router_ver1 = SimpleRouter()
router_ver1.register(r'api/v1/groups', GroupViewSet, 'Groups')
router_ver1.register(r'api/v1/posts', PostViewSet, 'Posts')
router_ver1.register(r'api/v1/posts/(?P<post_id>\d+)/comments',
                     CommentViewSet,
                     'Comment')

urlpatterns = [path('api-token-auth/', views.obtain_auth_token)]

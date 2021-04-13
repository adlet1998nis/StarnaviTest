from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()
router.register('posts', views.PostViewSet)
router.register('analytics', views.AnalyticsViewSet, basename='analytics')

urlpatterns = router.urls

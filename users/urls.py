from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view()),
]

router = SimpleRouter()
router.register('', views.RegisterViewSet, basename='register')
router.register('', views.UserInfoViewSet, basename='user-info')

urlpatterns += router.urls

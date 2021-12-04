from django.urls import include, path
from rest_framework import routers, urlpatterns
from . import views

router = routers.DefaultRouter()

router.register(r'tierlist', views.TierlistViewSet)
router.register(r'game', views.GameViewSet)
router.register(r'character', views.CharacterViewSet)
router.register(r'profile', views.ProfileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
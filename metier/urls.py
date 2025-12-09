from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PieceModelViewSet,ReparationModelViewSet

router=DefaultRouter()
router.register(r"piece",PieceModelViewSet)
router.register(r"reparation",ReparationModelViewSet)


urlpatterns = [
    path('',include(router.urls)),
]
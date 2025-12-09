from .views import faireReparation
from django.urls import path

urlpatterns = [
    path("reparation/<int:id>/<int:duree>/",faireReparation,name="fairereparation")
]

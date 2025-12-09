from django.shortcuts import render
from rest_framework import viewsets
from .models import Piece,Reparation
from .serializers import PieceSerializer,ReparationSerializer
# Create your views here.

class PieceModelViewSet(viewsets.ModelViewSet):
    queryset=Piece.objects.all()
    serializer_class=PieceSerializer
    
class ReparationModelViewSet(viewsets.ModelViewSet):
    queryset=Reparation.objects.all()
    serializer_class=ReparationSerializer
    

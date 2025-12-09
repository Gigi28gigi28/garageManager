from rest_framework import serializers
from .models import Piece,Reparation

class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Piece
        fields="__all__"
        

class ReparationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reparation
        fields="__all__"
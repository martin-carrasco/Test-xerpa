from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Player, Team
from .serializers import PlayerSerializer, TeamSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


        


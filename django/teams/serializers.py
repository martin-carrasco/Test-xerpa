from rest_framework import serializers
from django.db.models import Sum
from .models import Player, Team

class TeamSerializer(serializers.ModelSerializer):
    team_goals = serializers.SerializerMethodField()
    class Meta:
        model = Team
        fields = '__all__'

    def get_team_goals(self, obj):
        res = Player.objects.filter(team=obj).aggregate(Sum('goals'))
        if not res['goals__sum']:
            return 0
        return res['goals__sum']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__' 
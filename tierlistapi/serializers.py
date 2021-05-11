from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Game, Tierlist

class TierlistSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    game = serializers.PrimaryKeyRelatedField(
        queryset=Game.objects.all()
    )

    class Meta:
        model = Tierlist
        fields = ('title', 'likes', 'date', 'user', 'game')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('name', 'platform', 'year')
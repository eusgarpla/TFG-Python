from re import U
from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import Game, Tierlist, Character, Profile

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

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    game = serializers.PrimaryKeyRelatedField(
        queryset=Game.objects.all()
    )

    class Meta:
        model = Character
        fields = ('name', 'version', 'game')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    class Meta:
        model = Profile
        fields = ('twitterAccount', 'contactInformation', 'user')
from rest_framework import viewsets
from .serializers import GameSerializer, ProfileSerializer, TierlistSerializer, CharacterSerializer
from .models import Profile, Tierlist, User, Character, Game

# Create your views here.

# Tierlist EPs
class TierlistViewSet(viewsets.ModelViewSet):
    queryset = Tierlist.objects.all()
    serializer_class = TierlistSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
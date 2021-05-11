from rest_framework import viewsets
from .serializers import GameSerializer, TierlistSerializer
from .models import Tierlist, User, Character, Game

# Create your views here.

# Tierlist EPs
class TierlistViewSet(viewsets.ModelViewSet):
    queryset = Tierlist.objects.all()
    serializer_class = TierlistSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
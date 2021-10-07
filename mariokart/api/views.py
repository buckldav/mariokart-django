from mariokart.models import Character
from rest_framework import viewsets
from mariokart.api.serializers import CharacterSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

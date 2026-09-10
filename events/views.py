from django.shortcuts import render

# Create your views here.
from events.permissions import IsOrganizerOrReadOnly
from rest_framework import viewsets
from events.models import Event
from events.serializers import EventSerializer
class EventAPI(viewsets.ModelViewSet):
    permission_classes=[IsOrganizerOrReadOnly]
    queryset=Event.objects.all()
    serializer_class=EventSerializer

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)
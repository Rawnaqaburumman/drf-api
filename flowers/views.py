from rest_framework import generics
from .models import Flowers
from .serializer import FlowersSerializer
from .permissions import IsAuthenticatedOrReadOnly

class FlowersListView(generics.ListCreateAPIView):
    queryset = Flowers.objects.all()
    serializer_class = FlowersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class FlowersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flowers.objects.all()
    serializer_class = FlowersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


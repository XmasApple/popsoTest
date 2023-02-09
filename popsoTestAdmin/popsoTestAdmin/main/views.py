from django.http import HttpResponse
from rest_framework import permissions
from rest_framework import viewsets

from .models import ParsedData
from .serializers import ParsedDataSerializer


# Create your views here.
def index(response):
    return HttpResponse("<h1>Popso Test Admin</h1>")


# class for API that returns all data sorted by date
class ParsedDataViewSet(viewsets.ModelViewSet):
    queryset = ParsedData.objects.all().order_by('-date')
    serializer_class = ParsedDataSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class for API that returns all data filtered by tag
class ParsedDataTagViewSet(viewsets.ModelViewSet):
    queryset = ParsedData.objects.all().order_by('-date')
    serializer_class = ParsedDataSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        tag = self.request.GET.get('tag', None)
        print("tag: ", tag)
        return ParsedData.objects.filter(tag=tag)

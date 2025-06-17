from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import mixins

class AnimalList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 generics.GenericAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AnimalDetail(gene)
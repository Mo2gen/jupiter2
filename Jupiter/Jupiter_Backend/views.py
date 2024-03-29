from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ForecastHour, ForecastRequest
from .serializer import ForecastHourSerializer, ForecastRequestSerializer

class ForecastHourViewSet(viewsets.ModelViewSet):
    queryset = ForecastHour.objects.all()
    serializer_class = ForecastHourSerializer

    def create(self, request, *args, **kwargs):
        # Check if the request data is a list (multiple objects) or a single object
        is_many = isinstance(request.data, list)

        if is_many:
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED if is_many else status.HTTP_200_OK)


class ForecastRequestViewSet(viewsets.ModelViewSet):
    queryset = ForecastRequest.objects.all()
    serializer_class = ForecastRequestSerializer

    def create(self, request, *args, **kwargs):
        # Check if the request data is a list (multiple objects) or a single object
        is_many = isinstance(request.data, list)

        if is_many:
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED if is_many else status.HTTP_200_OK)

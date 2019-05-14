from django.shortcuts import render
from .serializers import CarSerializer
from .models import Car
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

def homepage(request):
    return render(request=request, template_name="main/home.html")

def carspage(request):
    return render(request=request, template_name="main/carpage.html",
    context={"car": Car.objects.all()})

class CarsApi(APIView):

    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = CarSerializer(cars,many=True)

        return Response(serializer.data)

    def post(self, requst, format=None):
        serializer = CarSerializer(data=requst.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDetail(APIView):

    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        car = self.get_object(pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def put(self, requst, pk, format=None):
        car = self.get_object(pk)
        serializer = CarSerializer(car, data=requst.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        car = self.get_object(pk)
        car.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


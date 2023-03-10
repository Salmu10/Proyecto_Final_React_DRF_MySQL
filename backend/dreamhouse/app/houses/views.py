from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets

from .models import Category
from .serializers import CategorySerializer
from .models import House
from .serializers import HouseSerializer
from .models import HouseServices
from .serializers import HouseServicesSerializer
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from dreamhouse.app.core.permissions import IsAdmin

class CategoryView(viewsets.GenericViewSet):

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         self.permission_classes = [AllowAny]
    #     else:
    #         self.permission_classes = [IsAuthenticated, IsAdmin]
    #     return super(CategoryView, self).get_permissions()

    def getCategories(self, request):
        categories = Category.objects.all()
        categories_serializer = CategorySerializer(categories, many=True)
        return Response(categories_serializer.data)
    
    def getOneCategory(self, request, slug):
        category = Category.objects.get(slug=slug)
        category_serializer = CategorySerializer(category)
        return Response(category_serializer.data)
    
    def post(self, request):
        category = request.data.get('category')
        serializer = CategorySerializer(data=category)
        if (serializer.is_valid(raise_exception=True)):
            serializer.save()
        return Response(serializer.data)
    
    def put(self, request, slug):
        category = Category.objects.get(slug=slug)
        data = request.data.get('category')
        serializer = CategorySerializer(instance=category, data=data, partial=True)
        if (serializer.is_valid(raise_exception=True)):
            serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, slug):
        category = Category.objects.get(slug=slug)
        category.delete()
        return Response({'data': 'Category deleted successfully'})
    
class HouseView(viewsets.GenericViewSet):

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         self.permission_classes = [AllowAny]
    #     else:
    #         self.permission_classes = [IsAuthenticated, IsAdmin]
    #     return super(CategoryView, self).get_permissions()

    def getHouses(self, request):
        houses = House.objects.all()
        houses_serializer = HouseSerializer(houses, many=True)
        return Response(houses_serializer.data)
    
    def getOneHouse(self, request, slug):
        house = House.objects.get(slug=slug)
        house_serializer = HouseSerializer(house)
        return Response(house_serializer.data)
    
    def post(self, request):
        house = request.data.get('house')
        house_services = request.data.get('house_services')
        serializer = HouseSerializer.create(house_context=house, services_context=house_services)
        # serializer = HouseSerializer(data=house)
        return Response(HouseSerializer.to_House(serializer))
        # return Response(serializer)
        # print(serializer)
        # return Response("hola")
    
    def put(self, request, slug):
        house = House.objects.get(slug=slug)
        data = request.data.get('house')
        serializer = HouseSerializer(instance=house, data=data, partial=True)
        if (serializer.is_valid(raise_exception=True)):
            serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, slug):
        house = House.objects.get(slug=slug)
        house.delete()
        return Response({'data': 'House deleted successfully'})
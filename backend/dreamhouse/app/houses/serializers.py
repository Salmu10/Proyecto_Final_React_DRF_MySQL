from rest_framework import serializers
from .models import Category
from .models import House
from .models import HouseServices
from dreamhouse.app.users.models import User
from random import randint

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'name', 'image']

    def to_category(self, instance):
        return {
            "id": instance.id,
            "slug": instance.slug,
            "name": instance.name,
            "image": instance.image,
        }

class HouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        fields = ['id', 'category', 'image', 'location', 'place', 'latitude', 'longitude']

    def to_House(instance):
        return {
            "id": instance.id,
            "category": instance.category,
            "image": instance.image,
            "location": instance.location,
            "place": instance.place,
            "latitude": instance.latitude,
            "longitude": instance.longitude,
        }
    
    def create(house_context, services_context):

        category_name = house_context['category']
        category = Category.objects.get(name=category_name)

        if category is None:
            raise serializers.ValidationError('Category not found')

        house = House.objects.create(
                    category=category, 
                    image=house_context['image'], 
                    location=house_context['location'], 
                    place=house_context['place'],
                    latitude=house_context['latitude'],
                    longitude=house_context['longitude']
                )
        
        if house is None:
            raise serializers.ValidationError('Create house error')
        
        house.save()
        
        house_services = HouseServicesSerializer.create(context=services_context, house_id=house)

        if house_services is None:
            raise serializers.ValidationError('Create house services error')
        
        # print(house)

        return house
    

class HouseServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = HouseServices
        fields = ['id', 'house', 'rooms', 'bathrooms', 'pool', 'wifi', 'parking']

    def to_HouseServices(instance):
        return {
            "id": instance.id,
            "house": instance.house,
            "rooms": instance.rooms,
            "bathrooms": instance.bathrooms,
            "pool": instance.pool,
            "wifi": instance.wifi,
            "parking": instance.parking,
        }

    def create(context, house_id):

        house_services = HouseServices.objects.create(
                            house=house_id, 
                            rooms=context['rooms'], 
                            bathrooms=context['bathrooms'], 
                            pool=context['pool'],
                            wifi=context['wifi'],
                            parking=context['parking']
                        )
        
        house_services.save()
        
        return house_services

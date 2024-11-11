from rest_framework import serializers
from .models import Restaurant, Table, Reservation
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'



class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'



class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


    def created(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
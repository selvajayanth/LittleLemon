from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu,Booking
from django.utils.timezone import now
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        read_only_fields = ['id']
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
    def validate_booking_date(self,value):
        if value<now():
            raise serializers.ValidationError('Booking date can not be in the past')
        return value
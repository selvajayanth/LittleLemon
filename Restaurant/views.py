from django.shortcuts import render
from rest_framework import generics
from .models import Menu,Booking
from rest_framework import viewsets
from .serializer import MenuSerializer,BookingSerializer
from rest_framework import permissions
# Create your views here.
def index(request):
    return render(request,'index.html',{})
def home(request):
    return
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

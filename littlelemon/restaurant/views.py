from django.shortcuts import render

from rest_framework.decorators import api_view,permission_classes
from .serializers import MenuItemSerializer,BookingViewSerializer
from rest_framework import generics, viewsets
from .models import Menu, Booking
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]  # This line sets the permission classes
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Booking.objects.all()
    serializer_class = BookingViewSerializer

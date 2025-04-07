from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.response import Response

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.models import User, Group



# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# handles post and get
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # def get_permissions(self):
    #     permission_classes = []
    #     if self.request.method != 'GET':
    #         permission_classes = [IsAuthenticated]
    #     return Response(permission() for permission in permission_classes)

#handles get, put and delete
class SingleMenuItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    # def get_permissions(self):
    #     permission_class = []
    #     if self.request.method != 'GET':
    #         permission_class = [IsAuthenticated]
    #     return Response(permission() for permission in permission_class)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

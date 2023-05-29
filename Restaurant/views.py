from datetime import datetime

from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .forms import BookingForm
from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuSerializer


# Create your views here.
def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, "menu.html", {"menu": menu_items})


def display_menu_item(request, pk=None):
    if pk:
        menu_item = MenuItem.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, "menu_item.html", {"menu_item": menu_item})


def booking(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "book.html", {"form": form})


# API views


class MenuView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer


class SingleItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer


class BookingView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    # def get(self, request):
    #     if request.GET.get("date") is not None:
    #         date = request.query_params.get("date")
    #     else:
    #         date = datetime.today().date()

    #     self.queryset = self.queryset.filter(booking_date=date)
    #     return super().get(request)


class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

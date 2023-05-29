from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("book/", views.booking, name="book"),
    path("menu/", views.menu, name="menu"),
    path("menu_item/<int:pk>/", views.display_menu_item, name="menu_item"),
    # API paths
    path("api/menu/", views.MenuView.as_view()),
    path("api/menu/<int:pk>", views.SingleItemView.as_view(), name="menu-item"),
    path("api/bookings", views.BookingView.as_view(), name="bookings"),
    path("api/bookings/<int:pk>", views.SingleBookingView.as_view(), name="booking-detail"),
]

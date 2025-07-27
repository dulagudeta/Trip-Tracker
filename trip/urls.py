from django.urls import path
from .views import HomeView, trips_list
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', trips_list, name='trip-list'),
]
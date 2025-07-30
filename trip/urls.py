from django.urls import path
from .views import HomeView, trips_list, TripCreateView, TripDetailView, NoteDetailView, NoteListView, NoteCreateView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', trips_list, name='trip-list'),
    path('dashboard/note/', NoteListView.as_view(), name='note-list'),
    path('dashboard/note/create/', NoteCreateView.as_view(), name='note-create'),
    path('dashboard/trip/create/', TripCreateView.as_view(), name='trip-create'),
    path('dashboard/trip/<int:pk>/', TripDetailView.as_view(), name='trip-detail'),
    path('dashboard/note/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
]
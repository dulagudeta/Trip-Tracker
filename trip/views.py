from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView , UpdateView ,DeleteView
from .models import Trip, Note

# Create your views here.
class HomeView(TemplateView):
    template_name = 'trip/index.html'

def trips_list(request):
    trips = Trip.objects.filter(owner=request.user)
    context = {
        'trips': trips
    }
    return render(request, 'trip/trips_list.html', context)

class TripCreateView(CreateView):
    model = Trip
    success_url= reverse_lazy('trip_list')
    fields = ['city', 'country', 'start_date', 'end_date']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form) 

class TripDetailView(DetailView):
    model = Trip
    template_name = 'trip/trip_detail.html'
    context_object_name = 'trip'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(trip=self.object) 
        return context
    
class NoteDetailView(DetailView):
    model = Note
    template_name = 'trip/note_detail.html'
    context_object_name = 'note'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trip'] = self.object.trip
        return context
    
class NoteListView(ListView):
    model = Note
    template_name = 'trip/note_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(trip__owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trips'] = Trip.objects.filter(owner=self.request.user)
        return context

class NoteCreateView(CreateView):
    model = Note
    fields = '__all__'
    success_url = reverse_lazy('note_list')
    
    def get_form(self):
        form = super(NoteCreateView, self).get_form()
        form.fields['trip'].queryset = Trip.objects.filter(owner=self.request.user)
        return form 
    
class NoteUpdateView(UpdateView):
    model = Note
    fields = '__all__'
    success_url = reverse_lazy('note_list')
    
    def get_form(self):
        form = super(NoteUpdateView, self).get_form()
        form.fields['trip'].queryset = Trip.objects.filter(owner=self.request.user)
        return form 
    
class NoteDeleteview(DeleteView):
    model = Note
    success_url = reverse_lazy('note_list')
    

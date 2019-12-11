from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Person, City
from .forms import PersonForm

#The view can be constructed using a FormView

class PersonListView(ListView):
    #the following is the same that queryset = Person.objects.all()
    model = Person
    context_object_name = 'people' #this is the name of the variable tha will be cought by 'person_list.html'
    #as ´template_name´ is not defined template code should be in hr/person_list.html. Take care of road

class PersonCreateView(CreateView):
    model = Person
    #We’re subclassing the generic class-based view CreateView. We specify the use of the built-in UserCreationForm and the not-yet-
    #  Created template at signup.html
    form_class = PersonForm
    #we use reverse_lazy to redirect the user to 'person_changelist' the log in page upon successful creation of neww Person 'hr/person_form.html'.
    success_url = reverse_lazy('person_changelist')
    #as ´template_name´ is not defined template and we use reverse_lazy, it redirect to 'person_changelist' defined in hr.urls
class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')
     #as ´template_name´ is not defined template and we use reverse_lazy, it redirect to 'person_changelist' defined in hr.urls

def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'hr/city_dropdown_list_options.html', {'cities': cities})

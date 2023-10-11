from django.shortcuts import render
from .models import MyModel
from django.views.generic import ListView

# Create your views here.


class MyModelListView(ListView):
    model = MyModel
    template_name = 'mymodel_list.html'

    from django.views.generic import ListView
from .models import MyModel

class MyModelListView(ListView):
    model = MyModel
    template_name = 'mymodel_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)  # Print the context to the console
        return context





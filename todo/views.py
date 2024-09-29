from django.shortcuts import render
from .models import Todo
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


# Create your views here.
class MyView(ListView):
    model = Todo
    template_name = 'todo/index.html'


class TaskCreateView(CreateView):
    model = Todo
    template_name = 'todo/createtask.html'
    fields = '__all__'
    success_url = reverse_lazy('todo')


class TaskDetailView(DetailView):
    model = Todo


class TaskDeleteView(DeleteView):
    model = Todo
    template_name = 'todo/delete.html'
    success_url = reverse_lazy('todo')


class TaskSearchView(ListView):
    model = Todo
    template_name = 'todo/index.html'
    queryset = Todo.objects.all()

    def get_queryset(self):
        result = self.request.GET.get('search_term')
        return Todo.objects.filter(title__icontains=result)

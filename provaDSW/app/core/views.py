from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, CreateView, DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import *

# Create your views here.

class ListStudent(TemplateView):
    template_name = "list_student.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["student_list"] = Student.objects.all()
        return context

class EditStudent(UpdateView):
    model = Student
    fields = ['name', 'age', 'email']
    template_name = 'edit_student.html'
    success_url = reverse_lazy('list-students')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Student updated successfully.')
        return response


class StudentDetail(DetailView):
    model = Student
    template_name = 'student_detail.html'

class CreateStudent(CreateView):
    model = Student
    fields = ['name', 'age', 'email', 'city', 'courses']
    template_name = 'create_student.html'
    success_url = reverse_lazy('list-students')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Student created successfully.')
        return response

class DeleteStudent(DeleteView):
    model = Student
    template_name = 'confirm_delete_student.html'
    success_url = reverse_lazy('list-students')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Student removed successfully.')
        return super().delete(request, *args, **kwargs)
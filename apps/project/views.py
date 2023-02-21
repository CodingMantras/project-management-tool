from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

from .models import Project


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    template_name = 'project_form.html'
    fields = ('name', 'description', 'end_date',
              'assigned_to', 'status', 'is_active')
    success_url = reverse_lazy('project:project_list_url')
    login_url = settings.LOGIN_URL

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'
    login_url = settings.LOGIN_URL


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'
    login_url = settings.LOGIN_URL


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    template_name = 'project_form.html'
    fields = ('name', 'description')
    success_url = reverse_lazy('project:project_list_url')
    login_url = settings.LOGIN_URL


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('project:project_list_url')
    login_url = settings.LOGIN_URL

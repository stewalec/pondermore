from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import Http404

from .models import Pondering


class PonderingIndexView(LoginRequiredMixin, ListView):
    template_name = "ponderings/index.html"
    context_object_name = "latest_pondering_list"

    def get_queryset(self):
        queryset = Pondering.objects.filter(user=self.request.user).order_by("-created_at")
        query = self.request.GET.get('q')
        
        if query:
            queryset = queryset.filter(
                Q(content__icontains=query) | Q(author__icontains=query) | Q(reference__icontains=query)
            ).distinct()
        return queryset


class PonderingDetailView(LoginRequiredMixin, DetailView):
    model = Pondering
    template_name = "ponderings/detail.html"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    

class PonderingCreateView(LoginRequiredMixin, CreateView):
    model = Pondering
    template_name = "ponderings/form.html"
    fields = ["content", "author", "reference", "private"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PonderingUpdateView(LoginRequiredMixin, UpdateView):
    model = Pondering
    template_name = "ponderings/form.html"
    fields = ["content", "author", "reference", "private"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    

class PonderingDeleteView(LoginRequiredMixin, DeleteView):
    model = Pondering
    template_name = "ponderings/delete.html"
    success_url = reverse_lazy("ponderings:pondering-index")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user:
            raise Http404()
        return obj
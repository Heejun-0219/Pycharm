from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'targer_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        tmp_profile = form.save(commit=False)
        tmp_profile.user = self.request.user
        tmp_profile.save()

        return super().form_valid(form)

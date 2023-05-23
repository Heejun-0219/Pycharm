from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorator import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'targer_profile'
    form_class = ProfileCreationForm
    # detail에서 pk를 확인하기 때문에 다음 명령어가 바로 실행되지 않는다.
    # success_url = reverse_lazy('accountapp:detail')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        tmp_profile = form.save(commit=False)
        tmp_profile.user = self.request.user
        tmp_profile.save()

        return super().form_valid(form)

    def get_success_url(self):
      return reverse('accountapp:detail', kwargs={'pk' : self.object.user.pk})

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'targer_profile'
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'

    def get_success_url(self):
      return reverse('accountapp:detail', kwargs={'pk' : self.object.user.pk})
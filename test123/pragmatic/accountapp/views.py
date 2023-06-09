from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

has_ownership = [account_ownership_required, login_required]

@login_required()
# Create your views here.
def hello_world(request):
    # view파일에서 직접 요청을 만든다.
    # return HttpResponse('Hello World')
    # 'DIRS': [os.path.join(BASE_DIR, 'templates')],

    # POST | GET
    if request.method == "POST":
        tmp = request.POST.get('hello_world_input')
        world = HelloWorld()
        world.text = tmp
        world.save()

        hello_world_objects_all = HelloWorld.objects.all() # django ORM - 객체 (ORM이란?)
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_objects_all})
        return HttpResponseRedirect(reverse('accountapp:hello_world')) # redirect get을 요청 // 다시 함수 호출
    else:
        hello_world_objects_all = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_objects_all})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # 계정 만드는 것에 성공했다면 어떤 주소로 다시 돌려줄 것인가 지정
    # reverse | reverse_lazy 클래스 내에서는 reverse를 바로 사용할 수 없다
    # reverse = 함수형 뷰
    # reverse_lazy = 클래스형 뷰
    # 라우팅을 해주는 기법
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

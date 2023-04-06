from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountapp.models import HelloWorld


# Create your views here.
def hello_world(request):
    # view파일에서 직접 요청을 만든다.
    # return HttpResponse('Hello World')
    # 'DIRS': [os.path.join(BASE_DIR, 'templates')],

    if request.method == "POST":
        tmp = request.POST.get('hello_world_input')
        world = HelloWorld()
        world.text = tmp
        world.save()

        hello_world_objects_all = HelloWorld.objects.all()
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_objects_all})
        return HttpResponseRedirect(reverse('accoutapp:hello_world'))
    else:
        hello_world_objects_all = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_objects_all})


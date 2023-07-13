from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"

urlpatterns = [
    # 라우팅
    # 함수형 뷰의 경우 그냥 함수의 이름만 넣어준다.
    # path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    # Login View | Logout View => next -> Login_ or Redirect or URL -> Default
    path('logout/', LogoutView.as_view(), name='logout'),

    # 클래스형 뷰는 다음과 같이 as_view()를 사용해준다.
    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]
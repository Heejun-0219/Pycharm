from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 해당 라인 위로는 클래스를 단순 상속받는 부분

        # 서버는 브라우저에서 오는 정보를 다 믿어서는 안된다.
        self.fields['username'].disabled = True

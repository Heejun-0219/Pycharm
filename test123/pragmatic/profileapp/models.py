from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    # user는 서버가 알아서 처리 (폼 사용 X)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)

    # model Form 기존에 있는 model을 폼으로 바꿔주는 방식
    # 커스터마이징 가능

from django.db import models

# Create your models here.

# python manage.py makemigrations
# python manage.py migrate = db 연동
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)
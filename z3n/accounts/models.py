from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # 추가 필드 (예: 전화번호)
    phone = models.CharField(max_length=15, blank=True, null=True)
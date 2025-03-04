from django.contrib import admin
from .models import CustomUser  # 사용자 모델 가져오기

admin.site.register(CustomUser)  # 관리자 페이지에 등록

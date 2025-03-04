from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)  # 이메일 필수 입력

    class Meta:
        model = get_user_model()  # 커스텀 유저 모델 대응
        fields = ('username', 'email', 'password1', 'password2')  # 폼 필드 지정

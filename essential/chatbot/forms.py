from django import forms
from .models import Chatbot

# ModelForm으로 모델에 맞는 폼 생성
class ChatbotForm(forms.ModelForm):
    
    class Meta:
        model = Chatbot
        fields = "__all__"
        exclude = ("author","bot_message")
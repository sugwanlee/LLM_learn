from django.urls import path
from . import views

app_name = "chatbot"
urlpatterns = [
    path("", views.chatbot_view, name="chatbot_view")
]

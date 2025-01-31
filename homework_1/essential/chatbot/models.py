from django.db import models

# Create your models here.
class Chatbot(models.Model):
    author = models.ForeignKey("user.Customuser", on_delete=models.CASCADE, related_name="chatbots")
    user_message = models.TextField()
    bot_message = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
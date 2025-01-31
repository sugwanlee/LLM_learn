from django.shortcuts import render
from .forms import ChatbotForm
from .models import Chatbot
from django.contrib.auth.decorators import login_required
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
    

response = openai.ChatCompletion.create(
	model="gpt-3.5-turbo",
	messages=[
			{"role": "system", "content": "You are a tour guide in Korea."},
			{"role": "user", "content": "제주도는 어떤곳이야?"}
		]
	)



@login_required
def chatbot_view(request):

    if request.method == "POST":
        chatbots = Chatbot.objects.all()
        form = ChatbotForm(request.POST)
        promft = [
			{"role": "system", "content": "You are a simple movie commenter"},
			{"role": "user", "content": request.POST.get('user_message') }
		        ]
        if form.is_valid():
            chatbot = form.save(commit=False)
            chatbot.author = request.user
            response = openai.ChatCompletion.create(
	                model="gpt-3.5-turbo",
	                messages=promft
	        )
            for chat in chatbots:
                promft.append({"role": "user", "content": chat.user_message })                
            chatbot.bot_message = response['choices'][0]['message']['content']
            chatbot.save()
            form = ChatbotForm()
            context = {
                "form" : form,
                "bot_message" : chatbot.bot_message,
            }
    else:
        form = ChatbotForm()
        context = {
        "form" : form
        }
    return render(request, "chatbot/chatbot.html", context)
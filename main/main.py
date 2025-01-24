import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = [
			{"role": "system", "content": "you are simple movie commenter"}
		]

while True:
    user_input = input("궁금한 것을 물어보세요 : ")
    if user_input.lower() != "exit":
        prompt.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=prompt
		)
        print(response['choices'][0]['message']['content'])
        with open("messages.txt", "a", encoding="utf-8") as file:
            file.write(f'질문 : {user_input}\n답변 : {response['choices'][0]['message']['content']}\n----------------\n')
    else:
        print("저희 서비스를 이용해주셔서 감사합니다!")
        break
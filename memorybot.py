import openai
import os
from dotenv import load_dotenv
import json

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

message_history = [{"role": "user", "content": f"You are an AI assistant. You will refer to the user by their name. You will answer questions based on the subject matter given"},
                   {"role": "assistant", "content": f"OK"}]
name = str(input("Please enter your name >: "))

def chat(inp, role = "user"):
    message_history.append({"role": role, "content": inp})

    completion = openai.chat.completions.create(
    model = "gpt-4.1-nano",
    messages = message_history,
    )

    reply_content = completion.choices[0].message.content
    print(f"OK {name}, {reply_content}")
    message_history.append({"role": "assistant", "content": reply_content})
    return reply_content

for i in range(2):
    user_input = input(">: ")
    print()
    chat(user_input)

with open("memory.txt", "w") as memory:
    json.dump({
        "name": name,
        "message_history": message_history
    }, memory, indent=2)
    


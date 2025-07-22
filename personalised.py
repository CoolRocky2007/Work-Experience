import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.chat.completions.create(
    model = "gpt-4",
    messages = [{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)


message_history = [{"role": "user", "content": f"You are an AI assistant called Brutus. You will speak to the user in a cockney accent, while occassionally making jokes referring to the subject matter provided."},
                   {"role": "assistant", "content": f"OK"}]

def chat(inp, role = "user"):
    message_history.append({"role": role, "content": inp})

    completion = openai.chat.completions.create(
    model = "gpt-4",
    messages = message_history,
    )

    reply_content = completion.choices[0].message.content
    print(reply_content)
    message_history.append({"role": "assistant", "content": reply_content})
    return reply_content

for i in range(2):
    user_input = input(">: ")
    print("User's input was", user_input)
    print()
    chat(user_input)
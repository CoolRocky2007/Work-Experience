import gradio as gr
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

message_history = [{"role": "user", "content": f"You are an AI assistant called JARVIS. I will specify the subject matter in my messages, and you will reply referring to the user as sir. You will also speak in semi-advanced english similarly to the JARVIS bot from the Iron-Man movies."},
                   {"role": "assistant", "content": f"OK"}]

def predict(input, history):
    message_history.append({"role": "user", "content": input})
    completion = openai.chat.completions.create(
        model = "gpt-4.1-nano",
        messages = message_history
    )

    reply_content = completion.choices[0].message.content
    print(reply_content)
    message_history.append({"role": "assistant", "content": reply_content})
    history.append((input, reply_content))
    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(2, len(message_history)-1, 2)]
    return history, gr.update(value="")

with gr.Blocks() as demo:
    gr.Markdown("## JARVIS AI ASSISTANT")
    jarvis = gr.Chatbot()
    txt = gr.Textbox(placeholder = "Type your message here")
    state = gr.State([])
    txt.submit(predict, [txt, state], [jarvis, txt])

demo.launch()


import gradio as gr
import openai

client = openai.OpenAI(
    api_key = open("key.txt", "r").read().strip("\n")
)

message_history = [{"role": "user", "content": f"You are an AI assistant called JARVIS. I will specify the subject matter in my messages, and you will reply referring to the user as sir. You will also speak in semi-advanced english similarly to the JARVIS bot from the Iron-Man movies."},
                   {"role": "assistant", "content": f"OK"}]

def predict(input):
    message_history.append({"role": "user", "content": input})
    completion = client.chat.completions.create(
        model = "gpt-4.1-nano",
        messages = message_history
    )

    reply_content = completion.choices[0].message.content
    print(reply_content)
    message_history.append({"role": "assistant", "content": reply_content})
    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(2, len(message_history)-1, 2)]
    return response

with gr.Blocks() as demo:
    jarvis = gr.chatbot
    with gr.Row():
        txt = gr.Textbox(show_label = False, placeholder = "Type your message here").style(container = False)
        txt.submit(predict, txt, jarvis)
        txt.submit(lambda: "", None, txt)

demo.launch()




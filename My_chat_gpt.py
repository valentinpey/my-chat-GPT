import openai
import tkinter as tk
from tkinter import scrolledtext

#le code suivant permet de recréer un chat GPT depuis GPT 3.5, en renvoyant toutes les infos précédentes au model
## une interface basic permet de faire une mimique de chatgpt
openai.api_key = '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'

conversation = []

def chat_with_gpt(message):
    global conversation

    conversation.append({"role": "user", "content": message})

    # Si la conversation est trop longue, supprimez les premiers messages.
    conversation_length = sum([len(msg["content"]) for msg in conversation])
    while conversation_length > 4096:
        removed_message = conversation.pop(0)
        conversation_length -= len(removed_message["content"])

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=50,
        temperature=0.6
    )

    conversation.append({"role": "assistant", "content": response.choices[0].message['content']})

    return response.choices[0].message['content']

def send():
    message = text_input.get()
    if message.lower() == "stop":
        root.quit()
    else:
        response = chat_with_gpt(message)
        text_box.config(state="normal")
        text_box.insert("end", "User: " + message + "\n")
        text_box.insert("end", "GPT: " + response + "\n")
        text_box.config(state="disabled")
    text_input.delete(0, "end")

def send_on_enter(event):
    send()

root = tk.Tk()
root.title("Mon chat GPT")

text_box = scrolledtext.ScrolledText(root)
text_box.config(state="disabled")
text_box.pack()

text_input = tk.Entry(root)
text_input.pack(side="left")
text_input.bind("<Return>", send_on_enter)

send_button = tk.Button(root, text="Send", command=send)
send_button.pack(side="right")

root.mainloop()
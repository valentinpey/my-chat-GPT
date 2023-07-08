import os
import openai
import tkinter as tk
from tkinter import scrolledtext
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationBufferWindowMemory


llm = ChatOpenAI(temperature=0.0, openai_api_key='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')
#trois type de création de memory
memory = ConversationBufferMemory()
#memory = ConversationBufferWindowMemory(k=1)  #k=1, specify how many previous exchanges you want to keep in memory (k=1 mean you will only get the previous exchange)             
#memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=30)

conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=True
)


def send():
    message = text_input.get()
    if message.lower() == "stop":
        root.quit()
    else:
        response = conversation.predict(input= message)
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
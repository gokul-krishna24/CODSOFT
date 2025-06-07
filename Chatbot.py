import tkinter as tk
from tkinter import scrolledtext

def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I'm a simple chatbot created by you!"
    elif "how are you" in user_input:
        return "I'm just code, but I'm doing fine. Thanks!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that."

def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_box.insert(tk.END, "You: " + user_input + "\n")
    response = get_bot_response(user_input)
    chat_box.insert(tk.END, "Bot: " + response + "\n\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Chatbot")
root.geometry("400x500")
root.config(bg="#F0F0F0")

chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
chat_box.pack(pady=10)
chat_box.config(state='normal')

entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack()

root.mainloop()

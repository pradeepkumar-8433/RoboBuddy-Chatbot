# Chatbot for your Help
import random

responses = {
    "hello": "Hello! How can I help you",
    "hi": "Hi there!",
    "how are you": "I'm just a chatbot, but I'm doing good!",
    "help": "What's help you want tell me!",
    "bye": "Goodbye! Have a good day!"
}

def chatbot():
    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break

        response = responses.get(user_input, "Sorry, I don't understand.")
        print(f"Chatbot: {response}")

chatbot()
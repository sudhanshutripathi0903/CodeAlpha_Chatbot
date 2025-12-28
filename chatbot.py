import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I am fine.", "Doing good.", "Great!"],
    "name": ["I am your Python Chatbot.", "You can call me Chatbot."],
    "bye": ["Goodbye!", "See you soon!", "Bye!"]
}

while True:
    user = input("You: ").lower()
    if user in responses:
        print("Bot:", random.choice(responses[user]))
    elif user == "exit" or user == "quit":
        print("Bot: Conversation ended.")
        break
    else:
        print("Bot: I don't understand that.")

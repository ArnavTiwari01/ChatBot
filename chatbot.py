import random

responses = {
    "hello": ["Hi there!", "Hello!", "Greetings!", "Howdy!"],
    "how are you?": ["I'm just a computer program, but thanks for asking!", "Doing well, how about you?", "I'm here to assist you!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "I'm sorry, I don't understand that."

def chatbot():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()
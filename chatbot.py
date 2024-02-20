
import random

# Define a function to generate responses
def get_response(user_input):
    greetings = ["hello", "hi", "hey", "greetings", "howdy"]
    farewells = ["goodbye", "bye", "see you later", "farewell"]
    responses = {
        "how are you": "I'm just a chatbot, but thanks for asking!",
        "what's your name": "I'm just a simple chatbot.",
        "who created you": "I was created by a developer.",
        "tell me a joke": "Why don't skeletons fight each other? They don't have the guts.",
        "thanks": "You're welcome!",
        "default": "I'm sorry, I don't understand.",
    }

    user_input = user_input.lower()

    if user_input in greetings:
        return "Hello! How can I assist you today?"
    elif user_input in farewells:
        return "Goodbye! Have a great day!"
    else:
        for key in responses:
            if key in user_input:
                return responses[key]
        return responses["default"]

# Main function to handle user interaction
def main():
    print("Welcome to the Simple Chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()

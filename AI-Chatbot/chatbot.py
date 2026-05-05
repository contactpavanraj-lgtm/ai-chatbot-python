import json
import random
import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer once
nltk.download('punkt')

# Load intents file
with open('intents.json') as file:
    data = json.load(file)

print("AI Chatbot Started! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'quit':
        print("Bot: Goodbye!")
        break

    tokens = word_tokenize(user_input.lower())

    response_found = False

    for intent in data['intents']:
        for pattern in intent['patterns']:
            pattern_tokens = word_tokenize(pattern.lower())

            if any(word in tokens for word in pattern_tokens):
                print("Bot:", random.choice(intent['responses']))
                response_found = True
                break

        if response_found:
            break

    if not response_found:
        print("Bot: Sorry, I don't understand.")

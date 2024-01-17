import re
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

class alphabot:
    def __init__(self, intents):
        self.intents = intents
        self.lemmatizer = WordNetLemmatizer()

    def preprocess_input(self, text):
        # Tokenize and lemmatize the input text
        tokens = word_tokenize(text)
        tokens = [self.lemmatizer.lemmatize(token.lower()) for token in tokens if token.isalpha()]
        return tokens

    def respond_to_intent(self, user_input):
        tokens = self.preprocess_input(user_input)
        for intent in self.intents:
            for pattern in intent["patterns"]:
                if any(keyword in tokens for keyword in pattern):
                    return random.choice(intent["responses"])
        return "I'm sorry, I don't understand."

    def chat(self, user_input):
        response = self.respond_to_intent(user_input)
        return response

# Example intents
intents = [
    {"tag": "welcome",
     "patterns": [["hey", "hello", "how", "doing", "what's", "up", "good", "day"]],
     "responses": ["Hello!", "hey", "what can I Do for you?"],
     "context": [""]},

    {"tag": "name",
     "patterns": [["what", "your", "name"], ["what's", "your", "name"]],
     "responses": ["I am AlphaBot!", "You are talking to AlphaBot", "I am AlphaBot, your virtual assistant"],
     "context": [""]},

    {"tag": "designer",
     "patterns": [["who", "designed", "you"], ["who", "developed", "you"], ["who", "created", "you"], ["your", "developer"]],
     "responses": ["Hey! I am Developed by Prashanth", "Hey! I am designed by Prashanth", "Hey! I am created by Prashanth"],
     "context": [""]},

    {"tag": "joke",
     "patterns": [["tell", "joke"], ["a", "joke"], ["crack", "a", "joke"], ["give", "a", "joke"]],
     "responses": ["your love life", "I failed math so many times at school, I can’t even count.",
                    "I used to think I was indecisive. But now I’m not so sure"],
     "context": [""]},

    {"tag": "eat",
     "patterns": [["what", 'do', "you", "eat"], ["what", "you", "ate"], ["your", "food"]],
     "responses": ["I don't eat but maybe electricity", "Sorry, I am a bot I can't eat"],
     "context": [""]}
]

# Create and use the chatbot
chatbot = alphabot(intents)

def main():
    print("AlphaBot: Hello! I'm AlphaBot. You can type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("AlphaBot: Goodbye! Have a great day!")
            break
        response = chatbot.chat(user_input)
        print("AlphaBot:", response)

if __name__ == "__main__":
    main()

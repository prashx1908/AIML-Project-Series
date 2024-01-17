import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

class AdmissionChatbot:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')

        self.intents = {
            'greeting': ['hello', 'hi', 'hey', 'greetings'],
            'procedures': ['procedure', 'process', 'how to apply'],
            'requirements': ['requirement', 'eligibility', 'qualifications'],
            'deadlines': ['deadline', 'application period'],
            'exit': ['exit', 'bye', 'goodbye']
        }

        self.admission_info = {
            'procedures': 'Admission procedures involve submitting your application online...',
            'requirements': 'To be eligible, you need to have a high school diploma and submit your transcripts...',
            'deadlines': 'The application deadline for the upcoming semester is on...',
        }

        self.user_context = {}

    def get_intent(self, user_input):
        tokens = word_tokenize(user_input)
        tagged_tokens = pos_tag(tokens)

        for intent, keywords in self.intents.items():
            for keyword in keywords:
                if any(tag.startswith('VB') or tag.startswith('NN') for _, tag in tagged_tokens) and keyword in tokens:
                    return intent

        return 'unknown'

    def get_response(self, intent):
        if intent == 'greeting':
            return "Hello! Ask me anything about college admission."
        elif intent == 'procedures':
            return self.admission_info['procedures']
        elif intent == 'requirements':
            return self.admission_info['requirements']
        elif intent == 'deadlines':
            return self.admission_info['deadlines']
        elif intent == 'exit':
            return "Goodbye!"
        else:
            return "I'm sorry, I don't have information about that. Please ask another question."

    def chat(self):
        print("Welcome to the Admission Chatbot! Ask me anything about college admission.")

        while True:
            user_input = input("You: ")

            intent = self.get_intent(user_input)
            response = self.get_response(intent)

            print("Chatbot:", response)

            if intent == 'exit':
                break

if __name__ == "__main__":
    chatbot = AdmissionChatbot()
    chatbot.chat()

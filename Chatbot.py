import nltk
import random
import string
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK datasets
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Predefined set of responses
responses = [
    "I'm here to chat with you!",
    "Tell me more about that.",
    "That's interesting, please go on.",
    "I'm just a simple chatbot, but I love talking with you!",
    "Could you elaborate a bit more?",
    "I see, what else can you tell me?",
    "What do you think about that?"
]
# Stopwords removal
stop_words = set(stopwords.words('english'))

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def preprocess_input(user_input):
    user_input = remove_punctuation(user_input)
    tokens = word_tokenize(user_input.lower())
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

def find_synonyms(word):
    synonyms = []
    for syn in wn.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms

def generate_response(user_input):
    tokens = preprocess_input(user_input)
    if not tokens:
        return "Sorry, I didn't quite get that. Could you rephrase?"
    
    # Check for synonyms and match to predefined responses
    for word in tokens:
        synonyms = find_synonyms(word)
        if any(synonym in user_input for synonym in synonyms):
            return random.choice(responses)

    # Default response
    return random.choice(responses)

def chatbot():
    print("Chatbot: Hi! How can I assist you today? (type 'bye' to end the conversation)")
    
    while True:
        user_input = input("You: ").lower()
        if user_input == 'bye':
            print("Chatbot: Goodbye! It was nice talking to you.")
            break
        
        response = generate_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()

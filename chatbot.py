import spacy

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

def process_input(user_input):
    # Process user input using spaCy
    doc = nlp(user_input)
    return doc

def generate_response(doc):
    # Simple rule-based responses based on spaCy analysis
    if any(token.pos_ in ['VERB', 'AUX'] for token in doc):
        return "That sounds interesting!"
    elif any(token.pos_ in ['NOUN', 'PROPN'] for token in doc):
        return "Tell me more about that."
    else:
        return "I'm not sure how to respond to that."

def main():
    print("spaCy Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'bye':
            print("spaCy Chatbot: Goodbye!")
            break

        doc = process_input(user_input)
        response = generate_response(doc)
        print("spaCy Chatbot:", response)

if __name__ == "__main__":
    main()


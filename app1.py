import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()


# Function to respond to user queries
def respond_to_query(query):
    # Tokenize the query
    tokens = word_tokenize(query)
    # Remove stopwords
    tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]

    # Check for keywords
    if 'hello' in tokens:
        response = "Hello! How can I assist you today?"
    elif 'thank' in tokens or 'thanks' in tokens:
        response = "You're welcome!"
    elif 'bye' in tokens:
        response = "Goodbye! Have a great day!"
    else:
        response = "I'm sorry, I didn't understand that."

    return response


# Function to speak the response
def speak(response):
    engine.say(response)
    engine.runAndWait()


# Main function
def main():
    print("Jarvis: Hello! How can I assist you today?")
    while True:
        # Get user input
        query = input("You: ")
        # Respond to query
        response = respond_to_query(query)
        print("Jarvis:", response)
        # Speak the response
        speak(response)
        # Break the loop if user says 'bye'
        if 'bye' in query.lower():
            break


if __name__ == "__main__":
    # Download NLTK resources if not already downloaded
    nltk.download('punkt')
    nltk.download('stopwords')
    # Run the main function
    main()

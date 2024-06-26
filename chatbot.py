import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def chatbot_response(user_input):
  """
  Handles user input and provides a response.
  """
  user_input = user_input.lower()  # Convert to lowercase
  tokens = nltk.word_tokenize(user_input)  # Tokenize the input
  lemmas = [lemmatizer.lemmatize(token) for token in tokens]  # Lemmatize words

  # Simple keyword-based responses
  if 'hello' in lemmas or 'hi' in lemmas:
    return "Hello! How can I assist you today?"
  elif 'time' in lemmas:
    return "Please provide your location for the current time."
  elif 'weather' in lemmas:
    return "Please specify a location for the weather forecast."
  else:
    return "I'm still learning. Can you rephrase your question?"

while True:
  user_input = input("You: ")
  if user_input.lower() == 'quit':
    break
  response = chatbot_response(user_input)
  print("Chatbot:", response)
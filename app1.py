import nltk
import spacy

nltk.download('wordnet')
nltk.download('stopwords')  # If you use stopwords
nltk.download('punkt')      # If you use sentence tokenization
nlp = spacy.load('en_core_web_sm')
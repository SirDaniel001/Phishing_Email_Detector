# preprocess_data.py
# --- Import Necessary Libraries ---
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import string

# --- Download NLTK Resources (First-Time Setup) ---
# This downloads a list of common stopwords (like 'the', 'is', 'and')
try:
    nltk.download('stopwords')
except:
    print("NLTK stopwords already downloaded.")

# --- Load the Cleaned Dataset ---
print("📁 Loading cleaned dataset...")
df = pd.read_csv('../data/spam_cleaned.csv')
print(f"Data shape: {df.shape}")
print(df['label'].value_counts())
print()

# --- Text Preprocessing Function ---
# This function will clean each individual message
def preprocess_text(text):
    # 1. Convert to lowercase
    text = text.lower()
    
    # 2. Remove punctuation and numbers (keep only letters)
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    
    # 3. Remove extra whitespace
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    
    return text

# --- Apply the Cleaning Function ---
print("🧹 Cleaning text messages...")
df['cleaned_message'] = df['message'].apply(preprocess_text)

# Let's see how the cleaning transformed the first message
print("Before cleaning:", df['message'].iloc[0])
print("After cleaning:", df['cleaned_message'].iloc[0])
print()

# --- Convert Labels to Numbers ---
# Machine learning models need numbers, not text labels
# ham -> 0, spam -> 1
df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})

# --- Split the Data into Training and Testing Sets ---
# We train the model on 80% of the data and save 20% to test its accuracy later
X_train, X_test, y_train, y_test = train_test_split(
    df['cleaned_message'],  # The features (our text messages)
    df['label_num'],        # The labels (0 or 1)
    test_size=0.2,          # 20% for testing
    random_state=42         # Seed for reproducibility (always get same split)
)

print(f"Training set size: {len(X_train)}")
print(f"Testing set size: {len(X_test)}")
print()

# --- TF-IDF Vectorization ---
# This is the magic that converts text to numbers
print("🔢 Converting text to TF-IDF features...")
tfidf_vectorizer = TfidfVectorizer(
    max_features=5000,      # Only consider top 5000 words
    stop_words='english',   # Remove English stopwords
    ngram_range=(1, 2)      # Consider single words and pairs of words
)

# Learn the vocabulary and transform training data
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)

# Transform the test data using the same vocabulary
X_test_tfidf = tfidf_vectorizer.transform(X_test)

print(f"TF-IDF training shape: {X_train_tfidf.shape}")
print(f"TF-IDF testing shape: {X_test_tfidf.shape}")
print()

# --- Save the Processed Data ---
# We'll save this for use in Day 3 (Model Training)
import joblib

joblib.dump(X_train_tfidf, '../data/X_train_tfidf.joblib')
joblib.dump(X_test_tfidf, '../data/X_test_tfidf.joblib')
joblib.dump(y_train, '../data/y_train.joblib')
joblib.dump(y_test, '../data/y_test.joblib')
joblib.dump(tfidf_vectorizer, '../models/tfidf_vectorizer.joblib')

print("💾 Saved processed data to '../data/'")
print("✅ Preprocessing complete! Data is ready for model training.")

# hybrid_system.py
import joblib
import re
import pandas as pd
import os
from sklearn.metrics import classification_report, accuracy_score

print("🤖🔍 Starting Day 5: Building Hybrid AI-Expert System")
print("="*55)

# --- Get the correct base directory path ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- Load the Optimized Model and Data ---
print("[1/5] Loading optimized model and test data...")
model_path = os.path.join(BASE_DIR, 'models', 'optimized_random_forest_model.joblib')
vectorizer_path = os.path.join(BASE_DIR, 'models', 'tfidf_vectorizer.joblib')
X_test_path = os.path.join(BASE_DIR, 'data', 'X_test_tfidf.joblib')
y_test_path = os.path.join(BASE_DIR, 'data', 'y_test.joblib')
data_csv_path = os.path.join(BASE_DIR, 'data', 'spam_cleaned.csv')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)
X_test = joblib.load(X_test_path)
y_test = joblib.load(y_test_path)

# --- Define Expert System Rules ---
print("[2/5] Defining expert system rules for phishing...")
# These are logical patterns that often appear in phishing messages
def expert_system_rules(text):
    """
    Applies rule-based logic to detect phishing indicators.
    Returns True if any rule is triggered (suspected phishing), False otherwise.
    """
    text = text.lower()
    rules_triggered = []
    
    # Rule 1: Urgency and pressure tactics
    urgency_keywords = ['urgent', 'immediately', 'action required', 'account suspended', 'verify now']
    if any(keyword in text for keyword in urgency_keywords):
        rules_triggered.append("Urgency language")
    
    # Rule 2: Financial incentives and prizes
    incentive_keywords = ['free', 'win', 'winner', 'prize', 'reward', 'million', 'cash','cashy']
    if any(keyword in text for keyword in incentive_keywords):
        rules_triggered.append("Financial incentive")
    
    # Rule 3: Suspicious requests
    request_keywords = ['password', 'click here', 'account verification', 'confirm your account', 'login']
    if any(keyword in text for keyword in request_keywords):
        rules_triggered.append("Suspicious request")
    
    # Rule 4: Poor grammar and excessive punctuation (common in spam)
    if re.search(r'!!+', text) or re.search(r'\?\?+', text) or re.search(r'\.\.+', text):
        rules_triggered.append("Excessive punctuation")
    
    # Rule 5: Currency symbols and large amounts
    if re.search(r'[\$\£\€]\s*\d+[,.]\d+', text):
        rules_triggered.append("Currency amount mentioned")
    
    # If any rules were triggered, return True (phishing suspected)
    return len(rules_triggered) > 0, rules_triggered

# --- Create Hybrid Prediction Function ---
print("[3/5] Creating hybrid prediction function...")
def hybrid_predict(message):
    """
    Makes a final prediction by combining AI model and expert system.
    """
    # First, get the AI's prediction and confidence
    message_tfidf = vectorizer.transform([message])
    ai_prediction = model.predict(message_tfidf)[0]
    ai_confidence = max(model.predict_proba(message_tfidf)[0])
    
    # Then, check the expert system rules
    rule_triggered, rules = expert_system_rules(message)
    
    # NEW SMARTER LOGIC:
    # 1. Always trust a high-confidence AI HAM prediction (to protect against false positives)
    if ai_prediction == 0 and ai_confidence > 0.85: 
        final_prediction = 0  # HAM
    # 2. If the AI says SPAM, OR if the AI is unsure and rules are triggered, classify as SPAM
    elif ai_prediction == 1 or (ai_confidence < 0.70 and rule_triggered):
        final_prediction = 1  # SPAM
    # 3. Otherwise, go with the AI's prediction
    else:
        final_prediction = ai_prediction
    
    return final_prediction, ai_prediction, rule_triggered, rules, ai_confidence

# --- Test the Hybrid System on a Few Examples ---
print("[4/5] Testing hybrid system with examples...")
test_messages = [
    "Congratulations! You've won a $1000 Amazon gift card. Click here to claim your prize now!",
    "Hi Daniel, are we still meeting for lunch tomorrow?",
    "URGENT: Your bank account has been suspended. Please verify your login credentials immediately.",
    "The project meeting is scheduled for 2 PM in conference room B."
]

print("\n   Hybrid System Test Results:")
print("   " + "-"*35)
for i, msg in enumerate(test_messages):
    final_pred, ai_pred, rule_trig, rules, confidence = hybrid_predict(msg)
    result = "SPAM" if final_pred == 1 else "HAM"
    print(f"   Example {i+1}: {result}")
    print(f"      AI Prediction: {'SPAM' if ai_pred == 1 else 'HAM'} ({confidence:.2%} confidence)")
    print(f"      Rules Triggered: {rules if rule_trig else 'None'}")
    print()

# --- Evaluate Hybrid System on Full Test Set ---
print("[5/5] Evaluating hybrid system on full test dataset...")
# Load the original test messages for rule checking
df_test = pd.read_csv(data_csv_path)
test_messages = df_test['message'].iloc[y_test.index]  # Align with the test labels

# Get predictions from both AI alone and the hybrid system
ai_predictions = model.predict(X_test)
hybrid_predictions = []

for message in test_messages:
    pred, _, _, _, _ = hybrid_predict(message)
    hybrid_predictions.append(pred)

hybrid_predictions = pd.Series(hybrid_predictions)

# Calculate accuracy
ai_accuracy = accuracy_score(y_test, ai_predictions)
hybrid_accuracy = accuracy_score(y_test, hybrid_predictions)

print("\n   PERFORMANCE COMPARISON:")
print("   " + "-"*25)
print(f"   AI-Alone Accuracy:    {ai_accuracy:.4f} ({ai_accuracy*100:.2f}%)")
print(f"   Hybrid System Accuracy: {hybrid_accuracy:.4f} ({hybrid_accuracy*100:.2f}%)")
print()

# Show classification report for the hybrid system
print("   Hybrid System Classification Report:")
print(classification_report(y_test, hybrid_predictions, target_names=['Ham', 'Spam']))

print("="*55)
print("🎉 Day 5 Complete! Hybrid AI-Expert system built and evaluated.")
print("💡 Next: Consider if the hybrid approach improved performance.")

# code/simple_detector.py
import joblib
import re
import os

# Get the correct base directory path
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'models', 'optimized_random_forest_model.joblib')

print("🤖 Loading AI model for Telegram bot...")

# Load model and vectorizer
model_path = os.path.join(BASE_DIR, 'models', 'optimized_random_forest_model.joblib')
vectorizer_path = os.path.join(BASE_DIR, 'models', 'tfidf_vectorizer.joblib')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

print("✅ Models loaded successfully!")

def expert_system_rules(text):
    """
    Applies rule-based logic to detect phishing indicators.
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
    
    return len(rules_triggered) > 0, rules_triggered

def simple_hybrid_predict(message):
    """
    Simplified version for Telegram bot - just prediction, no evaluation
    """
    # Get the AI's prediction and confidence
    message_tfidf = vectorizer.transform([message])
    ai_prediction = model.predict(message_tfidf)[0]
    ai_confidence = max(model.predict_proba(message_tfidf)[0])
    
    # Check the expert system rules
    rule_triggered, rules = expert_system_rules(message)
    
    # Decision logic
    if ai_prediction == 0 and ai_confidence > 0.85: 
        final_prediction = 0  # HAM
    elif ai_prediction == 1 or (ai_confidence < 0.70 and rule_triggered):
        final_prediction = 1  # SPAM
    else:
        final_prediction = ai_prediction
    
    return final_prediction, ai_prediction, rule_triggered, rules, ai_confidence

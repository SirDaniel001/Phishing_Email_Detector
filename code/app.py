# app.py
from flask import Flask, render_template, request
import joblib
import re
import os

# Initialize the Flask application
app = Flask(__name__, template_folder='../templates')

print("🌐 Starting Day 6: Web Application Development")
print("="*55)

# --- Get the correct base directory path ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_PATH = os.path.join(BASE_DIR, '..', 'static')
# --- Load the Model and Vectorizer ---
print("[1/4] Loading AI model and vectorizer...")
model_path = os.path.join(BASE_DIR, 'models', 'optimized_random_forest_model.joblib')
vectorizer_path = os.path.join(BASE_DIR, 'models', 'tfidf_vectorizer.joblib')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)
print("   ✅ Models loaded successfully")

# --- Define Expert System Rules (From Day 5) ---
print("[2/4] Loading expert system rules...")
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
    incentive_keywords = ['free', 'win', 'winner', 'prize', 'reward', 'million', 'cash']
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

# --- Create Hybrid Prediction Function (From Day 5) ---
print("[3/4] Loading hybrid prediction function...")
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
    
    # Intelligent decision logic:
    if ai_prediction == 0 and ai_confidence > 0.85: 
        final_prediction = 0  # HAM
    elif ai_prediction == 1 or (ai_confidence < 0.70 and rule_triggered):
        final_prediction = 1  # SPAM
    else:
        final_prediction = ai_prediction
    
    return final_prediction, ai_prediction, rule_triggered, rules, ai_confidence

# --- Define Flask Routes ---
print("[4/4] Setting up web routes...")
@app.route('/')
def home():
    """Render the home page with input form"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle form submission and return prediction results"""
    # Get the message from the form
    message = request.form['message']
    
    # Get prediction from hybrid system
    final_pred, ai_pred, rule_trig, rules, confidence = hybrid_predict(message)
    
    # Prepare results for display
    result = "PHISHING ATTEMPT DETECTED! 🚨" if final_pred == 1 else "LEGITIMATE MESSAGE ✅"
    ai_result = "SPAM" if ai_pred == 1 else "HAM"
    confidence_percent = f"{confidence * 100:.1f}%"
    
    return render_template('result.html', 
                         message=message,
                         result=result,
                         ai_result=ai_result,
                         confidence=confidence_percent,
                         rules_triggered=rules,
                         rules_found=rule_trig)

# === ADD THIS FAVICON ROUTE ===
@app.route('/favicon.ico')
def favicon():
    return ''  # Return empty response to stop 404 errors

print("   ✅ Web application setup complete!")
print("="*55)
print("🎉 Day 6 Complete! Web application is ready.")
print("💡 Run 'flask run' to start the server and visit http://127.0.0.1:5000")

if __name__ == '__main__':
    app.run(debug=True)

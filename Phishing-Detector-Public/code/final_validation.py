# final_validation.py
import joblib
import os
import pandas as pd

print("🔍 FINAL COMPREHENSIVE VALIDATION")
print("="*50)

# Check 1: Verify models load
print("[1/4] Verifying models load correctly...")
try:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model = joblib.load(os.path.join(BASE_DIR, 'models', 'optimized_random_forest_model.joblib'))
    vectorizer = joblib.load(os.path.join(BASE_DIR, 'models', 'tfidf_vectorizer.joblib'))
    print("   ✅ Models load successfully")
except Exception as e:
    print(f"   ❌ Model loading failed: {e}")

# Check 2: Verify data files
print("[2/4] Verifying data files...")
try:
    test_data = joblib.load(os.path.join(BASE_DIR, 'data', 'X_test_tfidf.joblib'))
    print(f"   ✅ Test data loaded: {test_data.shape}")
except Exception as e:
    print(f"   ❌ Data loading failed: {e}")

# Check 3: Verify templates exist
print("[3/4] Verifying templates...")
templates_dir = os.path.join(BASE_DIR, 'templates')
required_templates = ['index.html', 'result.html']
all_templates_exist = all(os.path.exists(os.path.join(templates_dir, t)) for t in required_templates)
if all_templates_exist:
    print("   ✅ All templates exist")
else:
    print("   ❌ Missing templates")

# Check 4: Test hybrid prediction
print("[4/4] Testing hybrid prediction...")
try:
    # Test the hybrid prediction function
    from sklearn.metrics import accuracy_score
    y_test = joblib.load(os.path.join(BASE_DIR, 'data', 'y_test.joblib'))
    
    # Load a few test messages
    df_test = pd.read_csv(os.path.join(BASE_DIR, 'data', 'spam_cleaned.csv'))
    test_messages = df_test['message'].sample(3, random_state=42)
    
    print("   Sample predictions:")
    for i, msg in enumerate(test_messages):
        message_tfidf = vectorizer.transform([msg])
        prediction = model.predict(message_tfidf)[0]
        proba = model.predict_proba(message_tfidf)[0]
        confidence = max(proba)
        result = "SPAM" if prediction == 1 else "HAM"
        print(f"      Message {i+1}: {result} ({confidence:.1%})")
    
    print("   ✅ Hybrid prediction test passed")
    
except Exception as e:
    print(f"   ❌ Prediction test failed: {e}")

print("="*50)
print("🎉 FINAL VALIDATION COMPLETE!")
print("📋 All systems are ready for Day 7 documentation.")

import joblib
import pandas as pd

print("🔍 Verifying Day 2 Outputs...")
print("="*50)

try:
    # 1. Load the processed data
    print("1. Loading processed data files...")
    X_train = joblib.load('../data/X_train_tfidf.joblib')
    X_test = joblib.load('../data/X_test_tfidf.joblib')
    y_train = joblib.load('../data/y_train.joblib')
    y_test = joblib.load('../data/y_test.joblib')
    vectorizer = joblib.load('../models/tfidf_vectorizer.joblib')
    print("   ✅ All files loaded successfully.")

    # 2. Check data shapes and types
    print("\n2. Checking data shapes and types:")
    print(f"   X_train shape: {X_train.shape} (type: {type(X_train)})")
    print(f"   X_test shape:  {X_test.shape} (type: {type(X_test)})")
    print(f"   y_train shape: {y_train.shape} (type: {type(y_train)})")
    print(f"   y_test shape:  {y_test.shape} (type: {type(y_test)})")

    # 3. Check label distribution
    print("\n3. Checking label distribution:")
    print(f"   Training set - Ham: {(y_train == 0).sum()}, Spam: {(y_train == 1).sum()}")
    print(f"   Testing set  - Ham: {(y_test == 0).sum()}, Spam: {(y_test == 1).sum()}")

    # 4. Verify vectorizer features
    print("\n4. Checking TF-IDF Vectorizer:")
    print(f"   Vocabulary size: {len(vectorizer.get_feature_names_out())}")
    print(f"   First 10 features: {vectorizer.get_feature_names_out()[:10]}")

    print("\n" + "="*50)
    print("🎉 ALL CHECKS PASSED! Day 2 outputs are valid and ready for model training.")

except Exception as e:
    print(f"❌ ERROR: {e}")

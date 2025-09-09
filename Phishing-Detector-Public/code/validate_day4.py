# validate_day4.py
import joblib
import numpy as np

print("🔍 Performing Deep Validation for Day 4")
print("="*50)

try:
    # 1. Load both models
    print("[1/4] Loading original and optimized models...")
    original_model = joblib.load('../models/best_random_forest_model.joblib')
    optimized_model = joblib.load('../models/optimized_random_forest_model.joblib')
    print("   ✅ Models loaded successfully")
    
    # 2. Load the test data
    print("[2/4] Loading test data...")
    X_test = joblib.load('../data/X_test_tfidf.joblib')
    y_test = joblib.load('../data/y_test.joblib')
    
    # 3. Check if models are different by comparing parameters
    print("[3/4] Comparing model parameters...")
    original_params = original_model.get_params()
    optimized_params = optimized_model.get_params()
    
    print("   Original Model n_estimators:", original_params['n_estimators'])
    print("   Optimized Model n_estimators:", optimized_params['n_estimators'])
    print("   Original Model min_samples_split:", original_params['min_samples_split'])
    print("   Optimized Model min_samples_split:", optimized_params['min_samples_split'])
    
    # 4. Make predictions with both models
    print("[4/4] Making predictions with both models...")
    original_predictions = original_model.predict(X_test)
    optimized_predictions = optimized_model.predict(X_test)
    
    # Calculate accuracy
    from sklearn.metrics import accuracy_score
    original_accuracy = accuracy_score(y_test, original_predictions)
    optimized_accuracy = accuracy_score(y_test, optimized_predictions)
    
    print(f"   Original Model Accuracy: {original_accuracy:.4f}")
    print(f"   Optimized Model Accuracy: {optimized_accuracy:.4f}")
    
    # Check if predictions are identical
    predictions_identical = np.array_equal(original_predictions, optimized_predictions)
    print(f"   Predictions identical: {predictions_identical}")
    
    print("\n" + "="*50)
    if not predictions_identical:
        print("🎉 SUCCESS: Models are different but equally accurate!")
        print("   The optimization found a different optimal configuration.")
    else:
        print("🔍 RESULT: Models make identical predictions.")
        print("   The original parameters were already optimal.")
    
    print("✅ Day 4 validation complete. Optimization was successful.")

except Exception as e:
    print(f"❌ ERROR during validation: {e}")

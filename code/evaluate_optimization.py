# evaluate_optimization.py
import joblib
from sklearn.metrics import classification_report, accuracy_score

print("📊 Evaluating Optimized Model vs. Original Model")
print("="*55)

# 1. Load the test data
print("[1/3] Loading test data...")
X_test = joblib.load('../data/X_test_tfidf.joblib')
y_test = joblib.load('../data/y_test.joblib')

# 2. Load both models
print("[2/3] Loading the original and optimized models...")
original_model = joblib.load('../models/best_random_forest_model.joblib')
optimized_model = joblib.load('../models/optimized_random_forest_model.joblib')

# 3. Make predictions with both models
print("[3/3] Making predictions and generating reports...")
original_predictions = original_model.predict(X_test)
optimized_predictions = optimized_model.predict(X_test)

# 4. Calculate and compare accuracy
original_accuracy = accuracy_score(y_test, original_predictions)
optimized_accuracy = accuracy_score(y_test, optimized_predictions)

print("\n🤖 MODEL PERFORMANCE COMPARISON")
print("   " + "-"*35)
print(f"   Original Model Accuracy:  {original_accuracy:.4f} ({original_accuracy*100:.2f}%)")
print(f"   Optimized Model Accuracy: {optimized_accuracy:.4f} ({optimized_accuracy*100:.2f}%)")
print()

# 5. Print detailed report for the optimized model
print("📈 Optimized Model Classification Report:")
print(classification_report(y_test, optimized_predictions, target_names=['Ham', 'Spam']))

print("="*55)
if optimized_accuracy > original_accuracy:
    print("🎉 SUCCESS: Optimization improved the model!")
elif optimized_accuracy == original_accuracy:
    print("🔍 RESULT: Optimization found an equally good model with different parameters.")
else:
    print("💡 NOTE: The original model is slightly better. The optimized parameters may be more generalizable.")

print("Day 4 is now fully complete.")

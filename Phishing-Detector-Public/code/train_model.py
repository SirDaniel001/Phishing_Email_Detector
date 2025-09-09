# train_model.py
# --- Import Necessary Libraries ---
import joblib
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd

print("🤖 Starting Day 3: Model Training & Evaluation")
print("="*55)

# --- Load the Processed Data from Day 2 ---
print("[1/4] Loading preprocessed data...")
X_train = joblib.load('../data/X_train_tfidf.joblib')
X_test = joblib.load('../data/X_test_tfidf.joblib')
y_train = joblib.load('../data/y_train.joblib')
y_test = joblib.load('../data/y_test.joblib')

print(f"   Training data: {X_train.shape}")
print(f"   Testing data:  {X_test.shape}")
print()

# --- Initialize the Machine Learning Models ---
print("[2/4] Training Machine Learning models...")
# Model 1: Naive Bayes - Fast and often works very well for text classification
nb_model = MultinomialNB()
# Model 2: Random Forest - Powerful and robust, can capture more complex patterns
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# --- Train the Models on the Training Data ---
print("   Training Naive Bayes model...")
nb_model.fit(X_train, y_train)

print("   Training Random Forest model... (This may take a minute)")
rf_model.fit(X_train, y_train)
print("   Training complete!")
print()

# --- Make Predictions on the Test Set ---
print("[3/4] Evaluating model performance on Test Set...")
# Predict using Naive Bayes
nb_predictions = nb_model.predict(X_test)
# Predict using Random Forest
rf_predictions = rf_model.predict(X_test)

# --- Evaluate and Compare Model Performance ---
print("\n   Naive Bayes Performance:")
print("   " + "-"*25)
nb_accuracy = accuracy_score(y_test, nb_predictions)
print(f"   Accuracy: {nb_accuracy:.4f} ({nb_accuracy*100:.2f}%)")
print("\n   Classification Report:")
print(classification_report(y_test, nb_predictions, target_names=['Ham', 'Spam']))

print("\n   Random Forest Performance:")
print("   " + "-"*25)
rf_accuracy = accuracy_score(y_test, rf_predictions)
print(f"   Accuracy: {rf_accuracy:.4f} ({rf_accuracy*100:.2f}%)")
print("\n   Classification Report:")
print(classification_report(y_test, rf_predictions, target_names=['Ham', 'Spam']))

# --- Determine the Best Model ---
print("[4/4] Selecting the best model...")
if nb_accuracy > rf_accuracy:
    best_model = nb_model
    best_model_name = "Naive Bayes"
    print(f"   ✅ Best model: Naive Bayes (Accuracy: {nb_accuracy:.4f})")
else:
    best_model = rf_model
    best_model_name = "Random Forest"
    print(f"   ✅ Best model: Random Forest (Accuracy: {rf_accuracy:.4f})")

# --- Save the Best Model for Future Use ---
model_filename = f'../models/best_{best_model_name.lower().replace(" ", "_")}_model.joblib'
joblib.dump(best_model, model_filename)
print(f"   💾 Best model saved as: {model_filename}")

print("="*55)
print("🎉 Day 3 Complete! The AI model is now trained and evaluated.")
print(f"📊 Next step: Analyze the results and prepare for the Expert System integration.")

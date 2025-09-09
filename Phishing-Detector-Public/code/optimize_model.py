# optimize_model.py
# --- Import Necessary Libraries ---
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd

print("⚙️ Starting Day 4: Model Optimization")
print("="*50)

# --- Load the Processed Data ---
print("[1/4] Loading preprocessed data...")
X_train = joblib.load('../data/X_train_tfidf.joblib')
y_train = joblib.load('../data/y_train.joblib')

print(f"   Training data: {X_train.shape}")
print()

# --- Define the Parameter Grid for Tuning ---
print("[2/4] Setting up hyperparameter tuning...")
# We'll test different combinations of these parameters
param_grid = {
    'n_estimators': [50, 100, 200],      # Number of trees in the forest
    'max_depth': [None, 10, 20],         # Maximum depth of each tree
    'min_samples_split': [2, 5],         # Minimum samples required to split a node
    'min_samples_leaf': [1, 2]           # Minimum samples required at a leaf node
}

# Initialize the base Random Forest model
rf = RandomForestClassifier(random_state=42)

# Set up GridSearchCV to find the best combination
# cv=3 means it will use 3-fold cross-validation
grid_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=3,                    # 3-fold cross-validation
    verbose=1,               # Shows progress
    n_jobs=-1                # Uses all available CPU cores
)

# --- Perform the Grid Search (This will take some time) ---
print("[3/4] Performing grid search (this may take 5-10 minutes)...")
print("   Testing different parameter combinations...")
grid_search.fit(X_train, y_train)

# --- Display the Best Parameters and Score ---
print("\n   Optimization complete!")
print(f"   Best parameters found: {grid_search.best_params_}")
print(f"   Best cross-validation score: {grid_search.best_score_:.4f}")
print()

# --- Train and Save the Optimized Model ---
print("[4/4] Training final model with best parameters...")
# Create a new model with the best parameters found
best_rf_model = grid_search.best_estimator_

# Save the optimized model
optimized_model_path = '../models/optimized_random_forest_model.joblib'
joblib.dump(best_rf_model, optimized_model_path)
print(f"   💾 Optimized model saved to: {optimized_model_path}")

print("="*50)
print("🎉 Day 4 Complete! Model optimization finished.")
print("📊 Next: Evaluate the optimized model's performance.")

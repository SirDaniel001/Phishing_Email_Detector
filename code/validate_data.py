import pandas as pd

# Try to load the cleaned data
try:
    df = pd.read_csv('../data/spam_cleaned.csv')
    print("✅ SUCCESS: Data loaded without errors!")
    print(f"Data shape: {df.shape}")
    print("\nFirst 3 rows:")
    print(df.head(3))
    print(f"\nLabels distribution:\n{df['label'].value_counts()}")
except Exception as e:
    print(f"❌ FAILED: {e}")

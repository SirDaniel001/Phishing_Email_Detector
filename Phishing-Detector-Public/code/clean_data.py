import pandas as pd

# List of encodings to try. 'latin-1' (also known as 'iso-8859-1') often works for these older datasets.
encodings_to_try = ['latin-1', 'iso-8859-1', 'cp1252']

for encoding in encodings_to_try:
    try:
        print(f"Trying encoding: {encoding}")
        # Try to read the file with the current encoding
        df = pd.read_csv(
            '../data/spam.csv',
            usecols=[0, 1],
            header=0,
            names=['label', 'message'],
            encoding=encoding
        )
        print(f"✅ Success with encoding: {encoding}")
        # If successful, break out of the loop
        break
    except UnicodeDecodeError as e:
        print(f"❌ Failed with {encoding}: {e}")
        # If all encodings fail, this will be the last message
        if encoding == encodings_to_try[-1]:
            print("All encodings failed. Please check the file manually.")
            exit(1)

# If we get here, we succeeded! Let's see the data.
print("\nDataset preview:")
print(df.head())

# Save the cleaned data
clean_data_path = '../data/spam_cleaned.csv'
df.to_csv(clean_data_path, index=False, encoding='utf-8') # Save as UTF-8 for future use

print(f"\n✅ Cleaned data saved to: {clean_data_path}")
print(f"Original shape: {df.shape}")

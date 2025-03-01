numeric_columns = [
    "Soil pH", "Nitrogen Fertilizer Used (kg/ha)", "Temperature (°C)", 
    "Rainfall (mm/month)", "Yield (kg/ha)", "Protein Deficiency Severity"
]

print("\nConverting numeric columns...")
for col in numeric_columns:
    data[col] = pd.to_numeric(data[col], errors="coerce")
    print(f"Converted {col}")

print("\nMissing Values in the Dataset:")
print(data.isnull().sum())


print("\nCleaned Dataset Preview (First 5 Rows):")
print(data.head())

from sklearn.model_selection import train_test_split
X = data[['Temperature (°C)', 'Rainfall (mm/month)', 'Soil pH', 'Nitrogen Fertilizer Used (kg/ha)']]
y_yield = data['Yield (kg/ha)']
y_protein = data['Protein Deficiency Severity']
X_train, X_test, y_yield_train, y_yield_test = train_test_split(X, y_yield, test_size=0.2, random_state=42)
X_train_p, X_test_p, y_protein_train, y_protein_test = train_test_split(X, y_protein, test_size=0.2, random_state=42)
print(X_train)
print(X_test)
print(y_yield_train)
print(y_protein_test)
print(y_protein_train)

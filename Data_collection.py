#DATA COLLECTION
import pandas as pd

file_path = "rice_crop_analysis.csv" 
try:
    data = pd.read_csv(file_path, sep="\t")  
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

print("\nFirst Five Rows of the Dataset:")
print(data.head())

print("Dataset Information:")
print(data.info())


if len(data.columns) == 1:
    print("\nSingle-column issue detected. Attempting to split columns...")
    data = data.iloc[:, 0].str.split("\t", expand=True)
    print("Columns split successfully!")

data.columns = [
    "Region", "Issue", "Weather", "Soil Type", "Rice Variety", "Soil pH", 
    "Nitrogen Fertilizer Used (kg/ha)", "Water Availability", "Temperature (°C)", 
    "Rainfall (mm/month)", "Yield (kg/ha)", "Protein Deficiency Severity"
]
print("\nUpdated Column Names:")
print(data.columns)

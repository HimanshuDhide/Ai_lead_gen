import requests
import pandas as pd

# The URL of  Flask API
url = "http://127.0.0.1:5000/batch_predict"

# Load the dataset
file_path = r"D:\ai employee\data\Lead_Scoring_test.csv"
df = pd.read_csv(file_path)

test_data = df.iloc[0, :29].tolist()  
data = {
    "features": test_data
}

response = requests.post(url, json=data)
print("Response Status Code:", response.status_code)
try:
    response_json = response.json()
    print("Response JSON:", response_json)
except Exception as e:
    print("Error with JSON response:", e)

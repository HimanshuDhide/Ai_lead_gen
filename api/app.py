from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
import os
app = Flask(__name__)

# Load the trained XGBoost model
with open(r"D:\ai employee\model\xgboost_model.pkl", "rb") as f:
    model = pickle.load(f)

# Define CSV file paths
input_csv = r"D:\ai employee\data\Lead_Scoring_test.csv"  # Input dataset
output_csv = r"D:\ai employee\result\high_priority_leads.csv"  # filtered leads

output_dir = os.path.dirname(output_csv)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# Feature names (29)
feature_columns = [
    "Lead Origin", "Lead Source", "Do Not Email", "Do Not Call", "TotalVisits",
    "Total Time Spent on Website", "Page Views Per Visit", "Last Activity", "Country",
    "Specialization", "How did you hear about X Education", "What is your current occupation",
    "What matters most to you in choosing a course", "Search", "Newspaper Article",
    "X Education Forums", "Newspaper", "Digital Advertisement", "Through Recommendations",
    "Tags", "Lead Quality", "Lead Profile", "City", "Asymmetrique Activity Index",
    "Asymmetrique Profile Index", "Asymmetrique Activity Score", "Asymmetrique Profile Score",
    "A free copy of Mastering The Interview", "Last Notable Activity"
]


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1) 
        probability = model.predict_proba(features)[0][1]
        return jsonify({"probability_of_generating_lead_in_%": round(probability * 100, 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/batch_predict", methods=["POST"])
def batch_predict():
    try:
        # Load the dataset
        df = pd.read_csv(input_csv)
        if len(df.columns) < 29:
            return jsonify({"error": "Insufficient columns in dataset"}), 400
        features = df.iloc[:, :29].values  

        probabilities = model.predict_proba(features)[:, 1]  # Get probability of class 1

        df["Lead_Score (%)"] = probabilities * 100

        # Filter leads with score >= 70%
        high_priority_leads = df[df["Lead_Score (%)"] >= 70]

        # Save high-priority leads to a new CSV file
        high_priority_leads.to_csv(output_csv, index=False)

        return jsonify({
            "message": f"Processed {len(df)} leads, saved {len(high_priority_leads)} high-priority leads.",
            "output_file": output_csv
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)

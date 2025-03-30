Overview

This project implements a lead scoring model using XGBoost. The model is exposed as a REST API, allowing users to send lead data, get a lead score prediction, and filter leads with scores above a certain threshold (e.g., 70%). The dataset contains 29 features.

Features

Machine Learning model trained using XGBoost.
REST API for predictions using Flask.
Batch processing for lead scoring, which processes the entire dataset and filters high-priority leads.
Saves high-priority leads (with scores > 70%) in a CSV file with the percentage of conversion.

Required Libraries
Flask
pandas
numpy
xgboost
scikit-learn
requests
os

Step-by-Step Installation
Follow these steps to set up and run the project:

1. Clone or Download the Project
First, clone or download the project repository to your local machine. You can either use Git or download the ZIP file from the project repository.

2. Install the Required Libraries
Navigate to the project directory in your terminal and install the required libraries using pip.
To install the dependencies, run the following command:
pip install -r requirements.txt

3. Load the Model
Ensure that you have the trained XGBoost model (xgboost_model.pkl) saved locally in the directory D:\ai employee\model\ (or update the path in your app.py accordingly if you're using a different location).

4. Run the Flask API
In the terminal, navigate to the project directory where the app.py file is located, then run the Flask API:
python app.py

If everything is set up correctly, you should see output indicating that the Flask app is running. The default URL will be:
http://127.0.0.1:5000

then run:
test_api.py

5. Access the Processed Leads
After the batch prediction runs, the system will generate a new CSV file named high_priority_leads.csv with leads having a probability above 70%. You can access the file in your project directory.

Available Endpoints:
POST /predict
Predicts the lead conversion probability for a single lead. Accepts JSON data with features (29 values) as input and returns the lead conversion probability as a percentage.

request example:
{"features": [1, 1, 0, 0, 2, 1532, 2, 5, 12, 1, 6, 3, 0, 0, 0, 0, 0, 0, 0, 19, 2, 3, 0, 1, 0, 14, 20, 1, 4, 0]}

response example:
{probability_of_generating_lead_in_%": 85.67}


POST /batch_predict
Processes the entire dataset, predicts the lead conversion probability for all rows, filters leads with probabilities above 70%, and saves them to a new CSV file with the conversion percentage included.

Request Example:
{"features": [1, 1, 0, 0, 2, 1532, 2, 5, 12, 1, 6, 3, 0, 0, 0, 0, 0, 0, 0, 19, 2, 3, 0, 1, 0, 14, 20, 1, 4, 0]}

response example:
Response JSON: {'message': 'Processed 9240 leads, saved 3553 high-priority leads.', 'output_file': 'high_priority_leads.csv'}

License
This project is licensed under the MIT License.

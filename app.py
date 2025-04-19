from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

# Load model + expected features
model = joblib.load('./model/churn_model.pkl')
model_features = joblib.load('./model/model_features.pkl')  # One-hot encoded column names

app = Flask(__name__)

def preprocess_input(json_data, model_features):
    df = pd.DataFrame([json_data])
    df_encoded = pd.get_dummies(df)

    # Add missing columns
    for col in model_features:
        if col not in df_encoded:
            df_encoded[col] = 0

    df_encoded = df_encoded[model_features]
    return df_encoded

@app.route('/predict', methods=['POST'])
def predict():
    try:
        json_data = request.get_json()

        if not json_data:
            return jsonify({'error': 'No input data provided'}), 400

        df_ready = preprocess_input(json_data, model_features)
        pred = model.predict(df_ready)[0]
        prob = model.predict_proba(df_ready)[0][1]

        return jsonify({
            'prediction': int(pred),
            'churn_risk_percent': round(prob * 100, 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 for local
    app.run(debug=False, host='0.0.0.0', port=port)
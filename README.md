# Customer Churn Prediction API 🚀

A lightweight Flask API to predict customer churn risk based on telecom data. Deployable via Render.com!

## 🔧 Usage

Send a POST request to `/predict` with customer details as JSON.

### Example input:
```json
{
        "SeniorCitizen": 0,
        "tenure": 5,
        "MonthlyCharges": 75.35,
        "TotalCharges": 350.75,
        "gender": "Male",
        "Partner": "No",
        "Dependents": "No",
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "Yes",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check"
      }
```
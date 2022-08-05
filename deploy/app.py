# encoding utf-8

from fileinput import filename
import joblib
import pickle
from flask import Flask, request, jsonify


# filename = '../models/lr.joblib'
filename = '../models/model.pkl'
model = pickle.load(open(filename, 'rb'))

def prepare_features(ride):
    # features = {}
    # features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    # features['trip_distance'] = ride['trip_distance']
    # return features
    features = ['Month', 'Occupation', 'Type_of_Loan', 'Credit_Mix',
       'Credit_History_Age', 'Payment_of_Min_Amount', 'Payment_Behaviour',
       'Monthly_Inhand_Salary', 'Num_Bank_Accounts',
       'Num_Credit_Card', 'Interest_Rate', 'Delay_from_due_date',
       'Num_Credit_Inquiries', 'Credit_Utilization_Ratio',
       'Total_EMI_per_month', 'Changed_Credit_Limit',
       'Amount_invested_monthly', 'Monthly_Balance', 'Num_of_Delayed_Payment',
       'Outstanding_Debt', 'Annual_Income', 'Num_of_Loan', 'Age']
    return features


def predict(features):
    # X = X[features]
    preds = model.predict(features)
    return preds[0]


app = Flask('credit-score-prediction')


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()

    # features = prepare_features(ride)
    pred = predict(ride)

    result = {
        'credit_score': pred
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
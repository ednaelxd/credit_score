#!/usr/bin/env python
# coding: utf-8

import requests

# ride = {
#     "PULocationID": 20,
#     "DOLocationID": 30,
#     "trip_distance": 40
# }

ride = {
 'Age': '23',
 'Amount_invested_monthly': '80.41529543900253',
 'Annual_Income': '19114.12',
 'Changed_Credit_Limit': '11.27',
 'Credit_History_Age': '22 Years and 1 Months',
 'Credit_Mix': '_',
 'Credit_Utilization_Ratio': 26.822619623699016,
 'Delay_from_due_date': 3,
 'Interest_Rate': 3,
 'Month': 'January',
 'Monthly_Balance': '312.49408867943663',
 'Monthly_Inhand_Salary': 1824.8433333333328,
 'Num_Bank_Accounts': 3,
 'Num_Credit_Card': 4,
 'Num_Credit_Inquiries': 4.0,
 'Num_of_Delayed_Payment': '7',
 'Num_of_Loan': '4',
 'Occupation': 'Scientist',
 'Outstanding_Debt': '809.98',
 'Payment_Behaviour': 'High_spent_Small_value_payments',
 'Payment_of_Min_Amount': 'No',
 'Total_EMI_per_month': 49.57494921489417,
 'Type_of_Loan': 'Auto Loan, Credit-Builder Loan, Personal Loan, and Home Equity Loan'}

url = 'http://127.0.0.1:5000/predict'
response = requests.post(url, json=ride)
print()
print(response)
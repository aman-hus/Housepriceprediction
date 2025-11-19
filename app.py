# Flask API
from flask import Flask,request,jsonify
import joblib,pandas as pd

app=Flask(__name__)
model=joblib.load('model.pkl')

@app.route('/')
def home():
    return "House Price Prediction API Running"

@app.route('/predict',methods=['POST'])
def predict():
    data=request.get_json()
    df=pd.DataFrame([data])
    pred=float(model.predict(df)[0])
    return jsonify({'prediction':pred})

if __name__=='__main__':
    app.run(debug=True)

# Streamlit UI
import streamlit as st
import joblib,pandas as pd

model=joblib.load('model.pkl')
st.title("House Price Prediction")

area=st.number_input("Area",200,5000,1000)
bed=st.number_input("Bedrooms",1,10,2)
age=st.number_input("Age",0,100,5)

if st.button("Predict"):
    df=pd.DataFrame({'area':[area],'bedrooms':[bed],'age':[age]})
    st.success(model.predict(df)[0])

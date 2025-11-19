# predict.py
import joblib, pandas as pd
model=joblib.load('model.pkl')
df=pd.DataFrame({'area':[1800],'bedrooms':[3],'age':[8]})
print("Predicted Price:",model.predict(df)[0])

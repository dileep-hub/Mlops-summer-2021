import joblib
mind = joblib.load('marks_Model.pkl')
mind.predict([[3]])
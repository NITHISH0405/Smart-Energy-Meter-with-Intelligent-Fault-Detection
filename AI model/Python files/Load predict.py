import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
data=pd.read_csv("EnergyMeterData.csv")
x=data[['Voltage(V)','Current (A)','Power Factor','Real Power (W)','Energy (kWh)','Apparent power(VA)']]
y=data['Appliance type']
x_train, x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
#print("Accuracy=",accuracy_score(y_test,y_pred))
sample=pd.DataFrame([{'Voltage(V)':230.0,'Current (A)':0.12,'Power Factor':0.85,'Real Power (W)':24,'Energy (kWh)':1.00,'Apparent power(VA)':28}])
prediction=model.predict(sample)
print("predicted Load Type= ",prediction[0])
joblib.dump(model,"load_type_model.pkl")
print("AI model saved")

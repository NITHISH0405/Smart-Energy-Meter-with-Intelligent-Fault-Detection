import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report\


data = pd.read_excel("FaultDetectionData.xlsx")
X = data[[
    "Voltage(V)",
    "Current(A)",
    "Power Factor",
    "Real Power(W)",
    "Apparent Power(VA)"
]]
y = data["Fault Status"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
model = RandomForestClassifier(
    n_estimators=300,
    class_weight="balanced",
    random_state=42
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy =", accuracy_score(y_test, y_pred))

print(classification_report(y_test, y_pred))
joblib.dump(model, "fault_model.pkl")

print("Fault model saved successfully!")

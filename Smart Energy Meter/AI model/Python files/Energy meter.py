import tkinter as tk
import pandas as pd
import joblib
import serial
# Load AI model


fault_model = joblib.load("fault_model.pkl")
load_model = joblib.load("load_type_model.pkl")
arduino=serial.Serial("COM3",9600)
#bt=serial.Serial("COM3",)
# -----------------------------
# Bill Calculation
# -----------------------------
def bill(energy):
    rate = 8.00
    return energy * rate

# -----------------------------
# Load Prediction
# -----------------------------
def predict(v, i, PF, p, e, ap):
          sample = pd.DataFrame([{
        "Voltage(V)": v,
        "Current (A)": i,
        "Power Factor": PF,
        "Real Power (W)": p,
        "Energy (kWh)": e,
        "Apparent power(VA)": ap}])
          prediction = load_model.predict(sample)
          return prediction[0]
        
def fault(voltage,current,pf,real_power,apparent):
    sample2=pd.DataFrame([{"Voltage(V)":voltage,"Current(A)":current,"Power Factor":pf,"Real Power(W)":real_power,"Apparent Power(VA)":apparent}])
    fault_prediction = fault_model.predict(sample2)[0]
    fault_confidence = fault_model.predict_proba(sample2).max()*100
    return fault_prediction
    


          
              
                   

# -----------------------------
# Update GUI
# -----------------------------
def update():

    # Sample values (Later these come from Arduino)
   data=arduino.readline().decode().strip()
   print(data)
   values=data.split("\t")
   voltage=float(values[0])
   current=float(values[1])
   pf=float(values[2])
   real_power=float(values[3])
   energy=float(values[4])
   apparent=float(values[5])
   load= predict(voltage, current, pf, real_power, energy, apparent)

   bill_amount = bill(energy)
   cond=fault(voltage,current,pf,real_power,apparent)

   voltage_label.config(text=f"Voltage : {voltage} V")
   current_label.config(text=f"Current : {current} A")
   pf_label.config(text=f"Power Factor : {pf}")
   power_label.config(text=f"Real Power : {real_power} W")
   a_power_label.config(text=f"Apparent Power : {apparent} VA")
   energy_label.config(text=f"Energy : {energy} kWh")
   load_label.config(text=f"Predicted Load Type :{load}  load")
   condition.config(text=f"Condition: {cond}")
   bill_label.config(text=f"Estimated Bill : ₹{bill_amount:.2f}")
   root.after(200,update)

# -----------------------------
# Create Window
# -----------------------------
root = tk.Tk()
root.title("AI Smart Energy Meter")
root.geometry("500x550")

# -----------------------------
# Title
# -----------------------------
title = tk.Label(root,
                 text="AI SMART ENERGY METER",
                 font=("Arial",20,"bold"),
                 fg="blue")

title.pack(pady=20)

# -----------------------------
# Labels
# -----------------------------
voltage_label = tk.Label(root, text="Voltage : 0 V", font=("Arial",18))
voltage_label.pack()

current_label = tk.Label(root, text="Current : 0 A", font=("Arial",18))
current_label.pack()

pf_label = tk.Label(root, text="Power Factor : 0", font=("Arial",18))
pf_label.pack()

power_label = tk.Label(root, text="Real Power : 0 W", font=("Arial",18))
power_label.pack()

a_power_label=tk.Label(root,text="Apparent Power : 0 VA", font=("Arial",18))
a_power_label.pack()

energy_label = tk.Label(root, text="Energy : 0 kWh", font=("Arial",18))
energy_label.pack()

load_label = tk.Label(root, text=" Load Type: -----", font=("Arial",18))
load_label.pack()

condition=tk.Label(root, text="Condtion:--------",font=("Arial",18))
condition.pack()

bill_label = tk.Label(root, text="Estimated Bill : ₹0.00", font=("Arial",18))
bill_label.pack()

# -----------------------------
# Update Button
# -----------------------------
'''update_button = tk.Button(root,
                          text="Update",
                          font=("Arial",14),
                          command=update)

update_button.pack(pady=20)
'''
update()
# -----------------------------
# Run Window
# -----------------------------
root.mainloop()

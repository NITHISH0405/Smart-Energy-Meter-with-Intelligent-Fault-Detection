# Smart Energy Meter with AI-Based Fault Detection

## Project Overview
- This project presents a **Smart Energy Meter with AI-Based Fault Detection** designed to monitor electrical parameters in real time and identify abnormal operating conditions using a machine learning model.
- The system measures **voltage, current, power factor, real power, apparent power, and energy consumption**. The measured parameters are displayed on a 16×2 LCD and can also be transmitted to a mobile device through Bluetooth. An AI-based fault detection model analyzes the electrical parameters and identifies whether the system is operating under normal or faulty conditions.

## Features

* Real-time monitoring of electrical parameters
* Voltage and current measurement
* Power factor calculation
* Real and apparent power calculation
* Energy consumption measurement
* Electricity bill approximation
* LCD-based parameter display
* Bluetooth-based wireless monitoring
* AI-based electrical fault detection
* Cost-effective and user-friendly implementation

## Hardware Used
* Arduino Uno R3
* ZMPT101B Voltage Sensor
* ACS712 Current Sensor
* 16×2 LCD
* HC-05 Bluetooth Module
* Push Button
* Voltage Regulator
* Power Supply

## Software & Technologies

* Arduino IDE
* Python
* Pandas
* Scikit-learn
* Joblib
* EmonLib
* Random Forest Classifier
 

## AI Model

A **Random Forest Classifier** is used for fault detection.

The model is trained using electrical parameters such as:

* Voltage
* Current
* Power Factor
* Real Power
* Apparent Power

The collected dataset is divided into training and testing data. After training and evaluation, the trained model is saved as a `.pkl` file and used for fault prediction.

## Working Principle

1. The voltage and current sensors measure the electrical parameters.
2. Arduino processes the sensor readings.
3. Real power, apparent power, power factor, and energy are calculated.
4. The results are displayed on the LCD.
5. The readings are transmitted to a mobile device through Bluetooth.
6. The electrical parameters are provided to the AI model.
7. The Random Forest model analyzes the parameters.
8. The system identifies the operating condition as **Normal or Fault**.


## Applications

* Residential energy monitoring
* Electrical fault monitoring
* Appliance monitoring
* Energy consumption analysis
* Small-scale commercial applications

## Future Improvements

* IoT and cloud-based monitoring
* Wi-Fi connectivity
* Three-phase energy monitoring
* Mobile fault notifications
* Predictive maintenance
* Smart home integration
* Improved AI-based load classification
Note: If you are using my code for your project. Kindly make sure that the PICKLE files and data sets are in the same folder for the code execution.



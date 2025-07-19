import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import tkinter as tk
from tkinter import messagebox

# Load and clean data
df = pd.read_csv(r"E:\python\salary\adult 3.csv")
df = df.replace(' ?', pd.NA).dropna()

# Encode categorical columns
label_encoders = {}
for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Features and target
X = df.drop("income", axis=1)
y = df["income"]

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# GUI App
def predict_income():
    try:
        user_input = {
            'age': int(age_entry.get()),
            'workclass': label_encoders['workclass'].transform([workclass_entry.get()])[0],
            'fnlwgt': int(fnlwgt_entry.get()),
            'education': label_encoders['education'].transform([education_entry.get()])[0],
            'educational-num': int(edu_num_entry.get()),
            'marital-status': label_encoders['marital-status'].transform([marital_entry.get()])[0],
            'occupation': label_encoders['occupation'].transform([occupation_entry.get()])[0],
            'relationship': label_encoders['relationship'].transform([relationship_entry.get()])[0],
            'race': label_encoders['race'].transform([race_entry.get()])[0],
            'gender': label_encoders['gender'].transform([gender_entry.get()])[0],
            'capital-gain': int(capital_gain_entry.get()),
            'capital-loss': int(capital_loss_entry.get()),
            'hours-per-week': int(hours_entry.get()),
            'native-country': label_encoders['native-country'].transform([country_entry.get()])[0],
        }

        input_df = pd.DataFrame([user_input])
        prediction = model.predict(input_df)[0]
        result = label_encoders['income'].inverse_transform([prediction])[0]
        messagebox.showinfo("Prediction", f"Predicted Income: {result}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create GUI window
root = tk.Tk()
root.title("Employee Salary Predictor")

fields = {
    "Age": None,
    "Workclass": None,
    "Fnlwgt": None,
    "Education": None,
    "Educational-num": None,
    "Marital-status": None,
    "Occupation": None,
    "Relationship": None,
    "Race": None,
    "Gender": None,
    "Capital-gain": None,
    "Capital-loss": None,
    "Hours-per-week": None,
    "Native-country": None
}

entries = {}

for i, field in enumerate(fields.keys()):
    tk.Label(root, text=field).grid(row=i, column=0, padx=5, pady=5, sticky='e')
    entry = tk.Entry(root, width=30)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries[field] = entry

# Assign entries to variables
age_entry = entries["Age"]
workclass_entry = entries["Workclass"]
fnlwgt_entry = entries["Fnlwgt"]
education_entry = entries["Education"]
edu_num_entry = entries["Educational-num"]
marital_entry = entries["Marital-status"]
occupation_entry = entries["Occupation"]
relationship_entry = entries["Relationship"]
race_entry = entries["Race"]
gender_entry = entries["Gender"]
capital_gain_entry = entries["Capital-gain"]
capital_loss_entry = entries["Capital-loss"]
hours_entry = entries["Hours-per-week"]
country_entry = entries["Native-country"]

# Predict button
tk.Button(root, text="Predict Income", command=predict_income, bg="lightblue").grid(row=len(fields), column=0, columnspan=2, pady=10)

root.mainloop()

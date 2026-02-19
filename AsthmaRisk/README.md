# 🫁 AsthmaGuard Pro

A simple Streamlit app that checks **asthma risk** using a machine learning model.
The user enters health details, environment details, and symptoms.
The app shows **risk percentage**, **charts**, and **basic advice**.

---

## ⭐ Features

* Predicts asthma risk using a trained model
* Easy slider inputs for age, BMI, pollution, symptoms, etc.
* Gauge chart to show risk percentage
* Radar chart to show different risk factors
* SHAP explainability to show which factor affects risk the most
* Clean and simple UI

---

## 📦 Requirements

Install all libraries:

```
pip install streamlit pandas numpy shap plotly matplotlib pickle5
```

(or from `requirements.txt` if you have one)

---

## ▶️ How to Run

1. Put the model file in the folder:

```
asthma_model_xgb.pkl
```

2. Run the app:

```
streamlit run app.py
```

3. The app will open in your browser:

```
http://localhost:8501
```

---

## 📂 Project Files

```
app.py                → main Streamlit app
asthma_model_xgb.pkl  → trained ML model
train_model.py        → script to train model (optional)
README.md             → project info
```

---

## 📝 Notes

* If the model file is missing, the app will show an error
* You must run `train_model.py` once to create the model

---
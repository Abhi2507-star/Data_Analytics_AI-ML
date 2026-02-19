import streamlit as st
import pandas as pd
import numpy as np
import pickle
import shap
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# --------------------------------------------------
# CONFIG & STYLE
# --------------------------------------------------
st.set_page_config(page_title="AsthmaGuard Pro", page_icon="🫁", layout="wide")

st.markdown("""
<style>
    .main { background-color: #f4f9ff; }
    .stButton>button { width: 100%; border-radius: 10px; height: 50px; font-weight: bold; }
    .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); margin-bottom: 20px; }
    h1 { color: #2C3E50; }
    h3 { color: #34495E; }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
@st.cache_resource
def load_data():
    try:
        model = pickle.load(open("asthma_model_xgb.pkl", "rb"))
        explainer = shap.TreeExplainer(model)
        return model, explainer
    except FileNotFoundError:
        return None, None

model, explainer = load_data()

if model is None:
    st.error("⚠️ Model not found! Please run 'python train_model.py' first.")
    st.stop()

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("🫁 AsthmaGuard Pro")
st.markdown("### AI-Powered Risk Assessment & Personalized Care")

col1, col2 = st.columns([1, 1.5], gap="large")

# --------------------------------------------------
# LEFT COLUMN: INPUTS
# --------------------------------------------------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📝 Patient Vitals")
    
    age = st.slider("Age", 5, 80, 30)
    bmi = st.slider("BMI", 15.0, 40.0, 22.5)
    fev1 = st.slider("Lung Function (FEV1)", 1.0, 5.0, 3.5, help="Normal is above 3.0L")
    activity = st.slider("Physical Activity (Hrs/Week)", 0, 10, 4)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🌫️ Environment & History")
    
    pollution = st.slider("Pollution (AQI Score 0-10)", 0.0, 10.0, 3.0)
    pollen = st.slider("Pollen Level (0-10)", 0.0, 10.0, 2.0)
    dust = st.slider("Dust Exposure (0-10)", 0.0, 10.0, 2.0)
    
    c1, c2 = st.columns(2)
    with c1:
        wheezing = st.checkbox("Wheezing?")
        smoking = st.checkbox("Smoker?")
    with c2:
        allergy = st.checkbox("Allergies?")
        family = st.checkbox("Family History?")
    
    st.markdown("---")
    st.caption("Derived Symptoms (Simplified for Demo)")
    short_breath = st.checkbox("Shortness of Breath")
    night_symp = st.checkbox("Nighttime Symptoms")
    st.markdown('</div>', unsafe_allow_html=True)

    # --------------------------------------------------
    # FEATURE ENGINEERING (Hidden Logic)
    # --------------------------------------------------
    vuln_idx = (int(wheezing)*2 + int(allergy)*1.5 + int(smoking)*1.2 + int(family)*1.0)
    env_idx = (pollution + pollen + dust) / 3
    symp_sev = (int(short_breath)*2 + int(night_symp)*2)
    life_risk = ((30 - 3*activity)*0.3 + (bmi - 25)*0.2 + 1.2)

    input_df = pd.DataFrame([{
        'Age': age, 'BMI': bmi, 'PhysicalActivity': activity, 'LungFunctionFEV1': fev1,
        'Env_Stress_Index': env_idx, 'Vulnerability_Index': vuln_idx, 
        'Symptom_Severity': symp_sev, 'Lifestyle_Risk': life_risk
    }])

    analyze_btn = st.button("🚀 Analyze Risk Profile")

# --------------------------------------------------
# RIGHT COLUMN: ANALYTICS
# --------------------------------------------------
with col2:
    if analyze_btn:
        # Prediction
        prob = model.predict_proba(input_df)[0][1]
        prediction = 1 if prob > 0.5 else 0

        # 1. SCORE CARD & GAUGE
        st.markdown('<div class="card">', unsafe_allow_html=True)
        ac1, ac2 = st.columns([2, 1])
        
        with ac1:
            st.subheader("Diagnosis Result")
            if prediction == 1:
                st.error(f"🔴 **HIGH RISK** (Confidence: {prob*100:.1f}%)")
                st.markdown("**Action:** Immediate preventive measures recommended.")
            else:
                st.success(f"🟢 **LOW RISK** (Confidence: {prob*100:.1f}%)")
                st.markdown("**Action:** Maintain routine monitoring.")

        with ac2:
            fig = go.Figure(go.Indicator(
                mode="gauge+number", value=prob*100,
                gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "#E74C3C" if prediction==1 else "#2ECC71"}}
            ))
            fig.update_layout(height=120, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # 2. RADAR CHART (Risk Factors)
        st.subheader("🎯 Risk Factor Radar")
        categories = ['Environment', 'Vulnerability', 'Symptoms', 'Lifestyle']
        values = [min(env_idx, 10), min(vuln_idx, 10), min(symp_sev, 10), min(life_risk, 10)]
        
        fig_radar = go.Figure(data=go.Scatterpolar(
            r=values, theta=categories, fill='toself', name='Patient'
        ))
        fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), height=300)
        st.plotly_chart(fig_radar, use_container_width=True)

        # 3. SHAP EXPLAINABILITY & ADVICE
        st.subheader("🤖 AI Personalized Advice")
        
        # Calculate SHAP
        shap_values = explainer.shap_values(input_df)
        if isinstance(shap_values, list): shap_values = shap_values[1]
        
        # Find Top Driver
        feature_names = input_df.columns
        # Handle SHAP array shape differences
        sv = shap_values[0] if len(shap_values.shape) > 1 else shap_values
        top_idx = np.argmax(np.abs(sv))
        top_feature = feature_names[top_idx]
        
        st.info(f"💡 The AI identified **{top_feature}** as the main driver of this result.")

        # Dynamic Advice Logic
        if top_feature == "Env_Stress_Index":
            st.warning("⚠️ **Advice:** High pollution impact detected. Install HEPA filters at home and wear masks outdoors.")
        elif top_feature == "LungFunctionFEV1":
            st.warning("⚠️ **Advice:** Lung capacity is low. Focus on breathing exercises and adhere to controller inhalers.")
        elif top_feature == "Lifestyle_Risk":
            st.warning("⚠️ **Advice:** BMI and inactivity are contributing factors. Consider a weight management plan.")
        elif top_feature == "Vulnerability_Index":
            st.warning("⚠️ **Advice:** Clinical history (Smoking/Allergies) is elevating risk. Smoking cessation is critical.")
        else:
            st.success("✅ **Advice:** No single critical factor detected. Keep maintaining a healthy lifestyle.")

    else:
        st.info("👈 Please adjust patient details and click 'Analyze Risk Profile'")
        st.image("https://img.freepik.com/free-vector/doctor-examining-patient-clinic-illustrated_23-2148856559.jpg", width=400)
#cd "C:\Users\Dell\OneDrive\Desktop\task 1 nti\student performance\07_Student_Performance_Index_Regression" && "C:\Users\Dell\AppData\Local\Programs\Python\Python311\python.exe" -m streamlit run app.py
import json
import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title='Student Performance Index Regression', layout='centered')

@st.cache_resource
def load_artifacts():
    model = joblib.load('best_model.pkl')
    with open('model_metadata.json', 'r', encoding='utf-8') as f:
        meta = json.load(f)
    return model, meta

model, meta = load_artifacts()
st.title(meta['project_title'])
st.caption(f"Task: {meta['task_type'].capitalize()} | Best Model: {meta['best_model_name']}")

with st.expander('Model Performance Metrics', expanded=False):
    st.json(meta['metrics'])

st.subheader('Input Features')
user_inputs = {}
for col in meta['numeric_features']:
    stats = meta['feature_ranges'][col]
    if stats['dtype'] == 'int':
        user_inputs[col] = st.number_input(col, min_value=int(stats['min']), max_value=int(stats['max']), value=int(stats['default']), step=1)
    else:
        user_inputs[col] = st.number_input(col, min_value=float(stats['min']), max_value=float(stats['max']), value=float(stats['default']))

for col in meta['categorical_features']:
    user_inputs[col] = st.selectbox(col, meta['categorical_options'][col])

if st.button('Predict', type='primary'):
    input_df = pd.DataFrame([user_inputs])
    prediction = model.predict(input_df)[0]
    if meta['task_type'] == 'classification':
        prob = model.predict_proba(input_df)[0][1]
        label = 'Positive (1)' if int(prediction) == 1 else 'Negative (0)'
        st.success(f'Prediction: {label} | Probability: {prob:.2%}')
    else:
        st.success(f"Predicted {meta['target_column']}: {prediction:,.2f}")

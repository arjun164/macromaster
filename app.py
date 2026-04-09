import streamlit as st
st.set_page_config(layout="wide")
st.title("MacroMaster v3.1")

sex = st.selectbox("Sex", ["Male", "Female", "Other"])
age = st.number_input("Age", 0, 150, 18)
unit = st.selectbox("Weight", ["kg", "lbs"])
w = st.slider("Weight", 0, 400, 108)
goal = st.selectbox("Goal", ["Cut", "Bulk", "Maintain"])

if st.button("Calculate"):
    wk = w if unit=="kg" else w*0.4536
    bmr = 10*wk + 6.25*180 - 5*age + 5 if sex=="Male" else 10*wk + 6.25*180 - 5*age - 161
if 'tdee' not in st.session_state:
    st.session_state.tdee = 2600  # your recomp goal
tdee = st.session_state.tdee

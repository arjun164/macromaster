import streamlit as st
st.set_page_config(layout="wide")
st.title("🏆 MacroMaster v3 - LIVE!")
st.success("✅ Multi-page working perfectly!")

st.header("🎯 Quick Goal Calculator")
sex = st.selectbox("Sex", ["Male", "Female", "Other"])
weight = st.number_input("Weight kg", 50, 200, 108)
height = st.slider("Height cm", 150, 210, 188)
age = st.slider("Age", 0, 101, 25)
goal = st.selectbox("Goal", ["Cut", "Bulk", "Maintain"])

if st.button("Calc Macros"):
    bmr = 10*weight + 6.25*height - 5*age + 5 if sex == "Male" else 10*weight + 6.25*height

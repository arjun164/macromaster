import streamlit as st
st.set_page_config(layout="wide")
st.title("🏆 MacroMaster v3.1")

# Top inputs
sex = st.selectbox("Sex", ["Male", "Female", "Other"])
age_input = st.number_input("Age", 0, 150, 18)  # renamed to avoid conflict
unit = st.selectbox("Weight Unit", ["kg", "lbs"])
w = st.slider("Weight", 0, 400, 108)
goal = st.selectbox("Goal", ["Cut", "Bulk", "Maintain"])

# Calculator (FIXED)
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (kg)", value=70)
    height = st.number_input("Height (cm)", value=175)
with col2:
    age = st.number_input("Age", value=19)  # local var OK here
    activity = st.selectbox("Activity", ["Sedentary (1.2)", "Moderate (1.55)", "Active (1.725)", "Very Active (1.9)"], 1)
    mult = float(activity.split()[1][1:-1])

if st.button("🚀 Calculate TDEE", use_container_width=True):
    bmr = 10*weight + 6.25*height - 5*age + 5  # Male formula
    tdee = bmr * mult
    st.session_state.tdee = tdee
    st.success(f"✅ TDEE: **{tdee:.0f}** cal/day")
    st.rerun()

# Safe default
if 'tdee' not in st.session_state:
    st.session_state.tdee = 2600
tdee = st.session_state.tdee

st.metric("Daily Target", f"{tdee:.0f} cal")  # Bonus display!

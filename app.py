import streamlit as st

st.set_page_config(layout="wide", page_title="MacroMaster")
st.title("🏆 MacroMaster v3.2 - Arjun's Fitness Tracker")

colA, colB = st.columns([1,2])
with colA:
    sex = st.selectbox("Sex", ["Male", "Female", "Other"])
    unit = st.selectbox("Weight Unit", ["kg", "lbs"])
    w = st.slider("Weight", 0, 400, 108, 1)
with colB:
    goal = st.selectbox("Goal", ["Cut (-500)", "Recomp", "Bulk (+300)"])

st.subheader("🚀 Calculate TDEE")
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (kg)", 40.0, 200.0, 70.0)
    height = st.number_input("Height (cm)", 140.0, 220.0, 175.0)
with col2:
    age = st.number_input("Age", 12, 80, 19)
    activity = st.selectbox("Activity", ["Sedentary (1.2)", "Moderate (1.55)", "Active (1.725)", "Very Active (1.9)"], 0)

if st.button("🚀 Calculate TDEE", use_container_width=True, type="primary"):
    # FIXED ORDER - Very Active FIRST!
    if "Very Active" in activity: mult = 1.9
    elif "Active" in activity: mult = 1.725
    elif "Moderate" in activity: mult = 1.55
    elif "Sedentary" in activity: mult = 1.2
    
    if sex == "Female": 
        bmr = 10*weight + 6.25*height - 5*age - 161
    else: 
        bmr = 10*weight + 6.25*height - 5*age + 5
    tdee = bmr * mult
    
    st.session_state.tdee = tdee
    st.session_state.bmr = bmr
    st.session_state.mult = mult
    st.session_state.weight = weight
    st.session_state.activity = activity
    
    st.success(f"✅ **TDEE: {tdee:.0f}** (BMR {bmr:.0f} × {mult})")
    st.info(f"Activity: {activity}")
    st.metric("Current TDEE", f"{tdee:.0f} cal")
    
    if st.button("🔄 Update & Continue", use_container_width=True):
        st.rerun()

if 'tdee' not in st.session_state:
    st.session_state.tdee = 2600
tdee = st.session_state.tdee

st.metric("📊 Daily Target", f"{tdee:.0f} calories")
st.caption("👈 Full app ready!")

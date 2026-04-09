import streamlit as st
st.header("🍽️ AI Meal Scanner")
uploaded = st.file_uploader("📸 Upload meal photo")
if uploaded:
    st.image(uploaded, use_column_width=True)
    st.success("AI estimate: Chicken rice = 45p/60c/12f/500kcal")
    st.columns(4)[0].button("✅ Add to log")

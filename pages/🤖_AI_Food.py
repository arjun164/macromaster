import streamlit as st
st.header("🤖 **AI Meal Scanner**")
st.markdown("*Upload photo → Instant macros*")

uploaded = st.file_uploader("📸 Upload meal", type=['jpg','png'])
if uploaded:
    st.image(uploaded, caption="Analyzing...", use_column_width=True)
    
    # Demo AI results (real Gemini API next)
    st.success("**AI Detection:**")
    col1, col2, col3 = st.columns(3)
    col1.metric("Chicken Rice", "45g protein")
    col2.metric("Rice Bowl", "60g carbs") 
    col3.metric("500kcal", "12g fat")
    
    if st.button("➕ Add to Tracker"):
        st.balloons()
        st.success("✅ Logged to daily totals!")

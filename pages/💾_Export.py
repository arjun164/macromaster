import streamlit as st
import pandas as pd

st.header("💾 Export Data")

# Your real data (from session_state)
if 'meals' not in st.session_state:
    st.session_state.meals = []

df = pd.DataFrame(st.session_state.meals, columns=['Date','Meal','Calories','Protein','Carbs','Fat'])

st.dataframe(df)

# PRO export
csv = df.to_csv(index=False)
st.download_button("📥 Download CSV", csv, "nutrition_log.csv", "text/csv")

st.caption("✅ All your AI scans + manual entries!")

import streamlit as st
import pandas as pd
import numpy as np

st.header("📈 **Progress Dashboard**")
st.markdown("*Weight trends, macro adherence, goal projection*")

# Weight chart
st.subheader("⚖️ Weight Progress")
weight_data = pd.DataFrame({
    'Week': [1,2,3,4,5],
    'Weight': [108,106.5,105,103.5,102]
})
st.line_chart(weight_data.set_index('Week'))

# Macro rings
st.subheader("📊 Today vs Goal")
col1, col2, col3 = st.columns(3)
col1.metric("Protein", "180/210g", "86%")
col2.metric("Carbs", "240/280g", "86%")
col3.metric("Calories", "2450/2850", "86%")

# Goal projection
st.subheader("🎯 88kg Projection")
st.info("12 weeks remaining at current pace")
st.progress(0.4)

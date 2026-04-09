import streamlit as st
import pandas as pd
st.header("📈 Progress Charts")
st.line_chart(pd.DataFrame({'Week': [1,2,3], 'Weight': [108,106,104]}))

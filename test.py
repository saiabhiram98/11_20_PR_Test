import streamlit as st
import pandas as pd

strike_df = pd.read_csv("STRIKE_REPORTS.csv", dtype= str)

st.dataframe(strike_df)
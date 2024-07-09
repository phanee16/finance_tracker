import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')
df = pd.read_sql('transaction', engine)

st.title('Personal Finance Tracker')
st.write('This is an interactive dashboard for visualizing your financial data.')

st.dataframe(df)

# Add more visualizations as needed

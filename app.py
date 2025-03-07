import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv('india.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')

st.sidebar.title('India Dataset Viz')

st.sidebar.selectbox('Select a state', list_of_states)


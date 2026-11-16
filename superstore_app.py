import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
st.title("superstore dashboard")
df = pd.read_csv("SampleSuperstore.csv")

st.dataframe(df.head(10))
st.write(df.describe())
st.plotly_chart(px.bar(df, x="Category" , y="Sales"))

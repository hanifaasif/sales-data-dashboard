import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Sales Data Analysis Dashboard")

df= pd.read_csv("Sales Data - Sales Data (1).csv")

st.write("Total Sales:",df["Sales"].sum())

st.dataframe(df.head(10))


         
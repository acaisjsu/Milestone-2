import streamlit as st
import pandas as pd
import numpy as np
# ChatGPT was used for coding help
st.title("Water Quality Data Uploader and Summary")
st.write("Upload a CSV file with water quality data.")

# Upload data
uploaded_file = st.file_uploader("Upload your water quality dataset (CSV)", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.write(df.head())

    # Calculate summaries
    summary = {}
    if 'pH' in df.columns:
        summary['pH'] = {
            'Average': round(df['pH'].mean(), 2),
            'Minimum': df['pH'].min(),
            'Maximum': df['pH'].max()
        }

    # Display summary statistics
    st.write("### Summary of Key Metrics")
    for metric, stats in summary.items():
        st.write(f"**{metric}**")
        for stat_name, stat_value in stats.items():
            st.write(f"{stat_name}: {stat_value}")
        st.write("")

   

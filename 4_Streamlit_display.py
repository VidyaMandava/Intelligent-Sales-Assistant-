# Databricks notebook source
#pip install streamlit
# dbutils.library.restartPython()

# COMMAND ----------

# Load the table back into a DataFrame
chat_completion_dataset2 = spark.table("chat_completion_dataset")

# COMMAND ----------

#converting to pandas df
chat_completion_dataset_pd = chat_completion_dataset2.toPandas()

# COMMAND ----------

import streamlit as st
import pandas as pd

# Set up the Streamlit page configuration
st.set_page_config(page_title="HCP Assignment Dashboard", layout="wide")

# Function to display HCP Briefing
def display_briefing(hcp_row):
    st.subheader(f"HCP: {hcp_row['HCP_Name']}")
    st.write(f"**Specialty**: {hcp_row['Specialty']}")
    st.write(f"**Preferred Drug**: {hcp_row['hcp_Preferred_Drug']}")
    st.write(f"**Communication Preference**: {hcp_row['Communication_Pref']}")
    st.write(f"**Preferred Meeting Type**: {hcp_row['Preferred_Meeting_Type']}")
    st.write(f"**Meeting Outcome**: {hcp_row['Meeting_Outcome']}")
    st.write(f"**Product Presented**: {hcp_row['Product_Presented']}")
    st.write(f"**Distance from Agent**: {round(hcp_row['Distance'], 2)} km")
    st.write(f"**Avg Daily Patients**: {hcp_row['Avg_Daily_Patients']}")
    
    # Prescription Patterns
    st.write("### 💊 Prescription Patterns:")
    st.table({
        "Drug": ["Drug A", "Drug B", "Drug C", "Other Drugs"],
        "Prescriptions": [
            hcp_row['Drug_A_Prescriptions'], 
            hcp_row['Drug_B_Prescriptions'], 
            hcp_row['Drug_C_Prescriptions'], 
            hcp_row['Other_Drugs_Prescriptions']
        ]
    })
    
    st.write(f"**Therapeutic Focus**: {hcp_row['Therapeutic_Focus']}")
    st.write(f"**Last Interaction Notes**: {hcp_row['Notes']}")
    

# Display Predictions
# def display_predictions(hcp_row):
#     st.write("### 🔮 Predictions")
#     # Add prediction data here if available
#     st.write("Predicted Engagement Level: High")
#     st.write("Recommended Action: Focus on Drug B promotion")

# Display Header
st.title("HCP Assignment & Briefing Dashboard")

# Filter for specific HCP (user input)
hcp_names = chat_completion_dataset_pd['HCP_Name'].unique()
selected_hcp = st.selectbox("Select HCP to view briefing", hcp_names)

# Filter the dataset based on selected HCP
hcp_row = chat_completion_dataset_pd[chat_completion_dataset_pd['HCP_Name'] == selected_hcp].iloc[0]

# Display HCP Briefing
st.write("## Briefing Pack")
display_briefing(hcp_row)

# Display Predictions
# st.write("## Predictions & Recommendations")
# display_predictions(hcp_row)

# Run the Streamlit app


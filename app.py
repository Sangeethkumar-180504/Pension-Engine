import streamlit as st
from main import calculate_benefits
import pandas as pd

# Page Config
st.set_page_config(page_title="Wipro DB Tech Tool", page_icon="💰")

st.title("💰 Pension & Gratuity Engine")
st.markdown("### *Specialized for Defined Benefit (DB) Tech Validation*")

# Sidebar for manual testing
st.sidebar.header("Individual Calculator")
user_name = st.sidebar.text_input("Employee Name", "Sangeethkumar")
user_salary = st.sidebar.number_input("Last Salary (₹)", min_value=0, value=50000)
user_years = st.sidebar.number_input("Years of Service", min_value=0, value=25)

if st.sidebar.button("Calculate Now"):
    # Using our main engine logic
    mock_row = pd.Series({'Salary': user_salary, 'Years': user_years})
    pension, gratuity = calculate_benefits(mock_row)
    
    st.success(f"Calculation Complete for {user_name}")
    c1, c2 = st.columns(2)
    c1.metric("Monthly Pension", f"₹{pension}")
    c2.metric("Total Gratuity", f"₹{gratuity}")

# Bulk processing section
st.divider()
st.subheader("📁 Bulk Data Processing")
if st.button("Process 'employees.csv'"):
    df = pd.read_csv('employees.csv')
    df[['Pension', 'Gratuity']] = df.apply(calculate_benefits, axis=1)
    st.dataframe(df.style.highlight_max(axis=0, color='#d4edda'))
    st.info("Verified results exported to 'processed_pensions.csv'")
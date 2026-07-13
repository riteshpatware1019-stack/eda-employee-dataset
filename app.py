import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Employee Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Employee Analytics Dashboard")

st.write("""
Welcome to the Employee Analytics Dashboard.

Use the menu on the left to explore:
- Dataset Overview
- Data Cleaning
- EDA
- Visualizations
- Business Insights
""")

st.title("Dataset Overview")
df=pd.read_csv("employees_data.csv")
st.dataframe(df)
st.write("Rows and Columns")
st.write(df.shape)
st.write(df.dtypes)


col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric("Employee",len(df))
with col2:
    st.metric("Average Salary",round(df["Salary"].mean(),2))
with col3:
    st.metric("Average Performance",round(df["Performance"].mean(),2))
with col4:
    st.metric("Average Attendance",round(df["Attendance"].mean(),2))


st.sidebar.header("Filters")
department=st.sidebar.selectbox(
    "Department",
    ["All"]+sorted(df["Department"].unique())
)
city=st.sidebar.selectbox(
    "City",
    ["All"]+sorted(df["City"].unique())
)


filtered=df.copy()

if department!="All":
    filtered=filtered[filtered["Department"]==department]

if city!="All":
    filtered=filtered[filtered["City"]==city]

st.subheader("Filtered Dataset")

st.dataframe(filtered)


st.subheader("Missing Values")
st.dataframe(df.isnull().sum())

st.subheader("Duplicate Rows")
st.write(df.duplicated().sum())


dept=filtered.groupby("Department")["Salary"].mean()
st.dataframe(dept)
fig,ax=plt.subplots(figsize=(8,5))
ax.bar(dept.index,dept.values)
ax.set_title("Average Salary by Department")
plt.xticks(rotation=45)
st.pyplot(fig)

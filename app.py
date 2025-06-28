import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("SampleSuperstore.csv")
st.title("Data Is Here")
st.file_uploader("upload your file", type=["csv"])

st.subheader("Data Preveiw")

st.sidebar.header(" Controls")
chart_type = st.sidebar.selectbox(
    "Select Chart Type",
    ["Bar Plot", "Scatter Plot", "Line Plot", "Box Plot"]
)

st.sidebar.subheader(" Filter Data")
min_value = st.sidebar.slider("Minimum Value", 0, 100, 0)

df = pd.DataFrame({
    "Category": ["A", "B", "C"],
    "Values": [10, 20, 15]
})
# df = pd.DataFrame({
#     'Values': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
# })
# df =pd.DataFrame({
#     'category': [""]
# })

filtered_df = df[df["Values"] >= min_value]

st.subheader("📋 Data Preview")
st.dataframe(filtered_df)

st.subheader("📈 Basic Statistics")
st.write(filtered_df.describe())

st.subheader(f"📊 {chart_type}")
fig, ax = plt.subplots(figsize=(10, 5))  
if chart_type == "Bar Plot":
    sns.barplot(x="Category", y="Values", data=filtered_df, ax=ax, palette="viridis")
elif chart_type == "Scatter Plot":
    sns.scatterplot(x="Categorys", y="Values", data=filtered_df, ax=ax, s=100, color="orange")
elif chart_type == "Line Plot":
    sns.lineplot(x="Category", y="Values", data=filtered_df, ax=ax, marker="o")
elif chart_type == "Box Plot":
    sns.boxplot(x="Category", y="Values", data=filtered_df, ax=ax)
else:
    st.error("Invalid chart type selected. Please choose a valid option.")

plt.title(f"{chart_type} of Values")
st.pyplot(fig)


st.markdown("---")
st.info("💡 **Tip:** Use the sidebar to customize the visualization.")

st.write("Column names:", df.columns.tolist())

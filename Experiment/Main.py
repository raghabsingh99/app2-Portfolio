import streamlit as st
import pandas
st.set_page_config(layout="wide")

st.title("The Best Company")
content = """Hi I am raghab singh. I am leraning python programming. In the context of data, "DE" typically stands 
    for Data Engineer. A Data Engineer is responsible for designing, building, and maintaining the infrastructure and systems 
    that enable the collection, storage, and analysis of data. 
    Their primary focus is on ensuring that data is accessible, reliable, and ready for use by data scientists, analysts, 
    and other stakeholders."""

st.info(content)
st.title("Our Team")
col1,emp_cola,col2,emp_colb,col3 = st.columns([1.5,0.5,1.5,0.5,1.5])
df = pandas.read_csv("data.csv",sep=",")
with col1:
    for index,row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()}{row["last name"].title()}')
        st.write(row["role"])
        st.image("images/"+row["image"])

with col2:
    for index,row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()}{row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index,row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()}'' {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])




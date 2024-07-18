import streamlit as st
import pandas
st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Raghab Singh")
    content = """Hi I am raghab singh. I am leraning python programming. In the context of data, "DE" typically stands 
    for Data Engineer. A Data Engineer is responsible for designing, building, and maintaining the infrastructure and systems 
    that enable the collection, storage, and analysis of data. 
    Their primary focus is on ensuring that data is accessible, reliable, and ready for use by data scientists, analysts, 
    and other stakeholders."""

    st.info(content)

content2 = """Below you can find some of the app I have built in python. Feel Free to contact me!Their primary focus is on ensuring that data is accessible, reliable, and ready for use by data scientists, analysts, 
    and other stakeholders.
"""
st.write(content2)

col3,col4 = st.columns(2)

df = pandas.read_csv("data.csv",sep=";")
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])





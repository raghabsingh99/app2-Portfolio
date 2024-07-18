import streamlit as st
st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Raghab Singh")
    content = """Hi I am raghab singh. I am leraning python programming. In the context of data, "DE" typically stands for Data Engineer. A Data Engineer is responsible for designing, building, and maintaining the infrastructure and systems that enable the collection, storage, and analysis of data. 
    Their primary focus is on ensuring that data is accessible, reliable, and ready for use by data scientists, analysts, 
    and other stakeholders."""
    st.info(content)
import streamlit as st


st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    # First dropdown
    dropdown1 = st.selectbox(
        "What topic do you want to discuss",
        ["Project Proposals", "Job Inqueires", "Other"]
    )
    message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

from {user_email}

{message}"""



    button = st.form_submit_button("Submit")
    if button:
        send_email=(message)
        st.info("Your email was sent successfully")


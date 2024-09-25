import pandas as pd
import streamlit as st
from typing import List, Dict
from models.utils import logger
from streamlit_js_eval import streamlit_js_eval

# Model imports
from models.sender import send_bulk_emails

st.set_page_config(layout="centered", page_title="Upload", page_icon="🛠️")


def submit_callback():
    st.session_state.submit_clicked = True


def refresh():
    streamlit_js_eval(js_expressions="parent.window.location.reload()")


def main():
    user_input = st.empty()

    # User input
    with user_input.container():
        st.subheader("Send Bulk Email:", divider="blue")
        text = st.text_area(label="Write your email")
        submit_btn = st.button(label="Submit", on_click=submit_callback)

    if "submit_clicked" not in st.session_state:
        st.session_state.submit_clicked = False

    if st.session_state.submit_clicked:

        user_input.empty()
        status = st.status(f"Sending Emails...")
        with status:
            success = send_bulk_emails(text)

        if success:
            st.success(body=f'Attendee info has been uploaded successfully', icon="🟢")


if __name__ == "__main__":
    main()

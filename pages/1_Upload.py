import pandas as pd
import streamlit as st
from typing import List, Dict
from models.utils import logger
from streamlit_js_eval import streamlit_js_eval

# Model imports
from models.airtable import upload_attendees

st.set_page_config(layout="centered", page_title="Upload", page_icon="🛠️")


def submit_callback():
    st.session_state.submit_clicked = True


def refresh():
    streamlit_js_eval(js_expressions="parent.window.location.reload()")


def main():
    user_input = st.empty()

    # User input
    with user_input.container():
        st.subheader("Upload a list of attendees:", divider="blue")
        original_csv = st.file_uploader(
            label="Please upload attendee info (.csv)",
            type="csv",
            accept_multiple_files=False,
            help="List of people you want to invite to this event",
        )
        submit_btn = st.button(label="Submit", on_click=submit_callback)

    if "submit_clicked" not in st.session_state:
        st.session_state.submit_clicked = False

    if st.session_state.submit_clicked:
        if not original_csv:
            st.error(body="Something is not right...", icon="🔴")
            st.stop()

        # Validate Lead List
        raw_list = pd.read_csv(original_csv).fillna("EMPTY")

        user_input.empty()
        with st.spinner('Uploading attendee info...'):
            success = upload_attendees(raw_list)

        if success:
            st.success(body=f'Attendee info has been uploaded successfully', icon="🟢")


if __name__ == "__main__":
    main()

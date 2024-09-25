import os
import yagmail
import streamlit as st
from typing import List
from models.airtable import get_attendee_emails


def send_bulk_emails(email: str):
    x = get_attendee_emails()
    yag = yagmail.SMTP(user="sndystudios@gmail.com", password=os.getenv("GMAIL_PASSWORD"))
    print(os.getenv("GMAIL_PASSWORD"))

    for attendee in x:
        contents = email.replace("[First Name]", attendee["name"])
        yag.send(to=attendee["email"], subject=f"Demo Test", contents=contents)
        st.write(f"Sent to {attendee['email']}")

    return True

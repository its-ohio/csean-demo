import os
import pandas as pd

from pprint import pprint
from typing import List, Dict
from pyairtable import Api
from dotenv import load_dotenv
from .utils import logger

# Airtable Setup
load_dotenv(".env.local")
airtable_client = Api(api_key=os.getenv("AIRTABLE_API_KEY"))
attendee_table = airtable_client.table(base_id="app8vn4TlQXUgSX7M", table_name='tblbi1HsaqgT6Pl9T')


def upload_attendees(data: pd.DataFrame) -> bool:
    # pprint(data)
    new_batch = []
    for index, row in data.iterrows():
        new_batch.append({"Email Address": row["Email Address"], "First Name": row["First Name"], "Last Name": row["Last Name"]})

    x = attendee_table.batch_create(new_batch)
    pprint(x)
    return True


def get_attendee_emails() -> List:

    res = attendee_table.all()
    attendees = []
    for record in res:
        temp = {"email": record["fields"]["Email Address"], "name": record["fields"]["First Name"]}
        attendees.append(temp)

    return attendees


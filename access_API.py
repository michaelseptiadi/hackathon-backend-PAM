import requests
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import datetime

URL = "https://apigw.withoracle.cloud/pamjaya/beta/account/"
auth = 'eyJ4NXQjUzI1NiI6Il96alE4UVJmS3dpSFduRkJYWkd0LVQ5NFAteElqOEtId0RCYk1lRmxjWVEiLCJ4NXQiOiJLbHhVMUFvcGdfb1VJZFEwYVVZdXpJUkdZaEUiLCJraWQiOiJTSUdOSU5HX0tFWSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI4ZDY5ZWM1ZjBkNmM0YzcyYmIwMzYzMmFhYWY5YzA2MiIsInNpZGxlIjo0ODAsImd0cCI6ImNjIiwidXNlci50ZW5hbnQubmFtZSI6ImlkY3MtNWNkMGM0YTU5M2JiNGE1ODk2NDMzNjdlN2NlMWRkN2UiLCJvcGMiOmZhbHNlLCJzdWJfbWFwcGluZ2F0dHIiOiJ1c2VyTmFtZSIsInByaW1UZW5hbnQiOnRydWUsImlzcyI6Imh0dHBzOlwvXC9pZGVudGl0eS5vcmFjbGVjbG91ZC5jb21cLyIsInRva190eXBlIjoiQVQiLCJjbGllbnRfaWQiOiI4ZDY5ZWM1ZjBkNmM0YzcyYmIwMzYzMmFhYWY5YzA2MiIsImNhX2d1aWQiOiJjYWNjdC0yMjg0YTk2N2M2N2E0NzYzYThlNWNmM2YxMGE4NmEyMCIsImF1ZCI6WyJodHRwczpcL1wvaGFja2F0aG9ub2ljLWF4dHpvdm5sdGNnYS1zaS5pbnRlZ3JhdGlvbi5vY3Aub3JhY2xlY2xvdWQuY29tOjQ0MyIsInVybjpvcGM6bGJhYXM6bG9naWNhbGd1aWQ9QThCRDAxMTE5QjIyNDczQjkzQ0JBQkYwMDQ2REUwNTQiLCJodHRwczpcL1wvQThCRDAxMTE5QjIyNDczQjkzQ0JBQkYwMDQ2REUwNTQuaW50ZWdyYXRpb24ub2NwLm9yYWNsZWNsb3VkLmNvbTo0NDMiXSwic3ViX3R5cGUiOiJjbGllbnQiLCJzY29wZSI6InVybjpvcGM6cmVzb3VyY2U6Y29uc3VtZXI6OmFsbCIsImNsaWVudF90ZW5hbnRuYW1lIjoiaWRjcy01Y2QwYzRhNTkzYmI0YTU4OTY0MzM2N2U3Y2UxZGQ3ZSIsInJlZ2lvbl9uYW1lIjoiYXAtc2luZ2Fwb3JlLWlkY3MtMSIsImV4cCI6MTY1ODU2NjYzMywiaWF0IjoxNjU4NTYzMDMzLCJjbGllbnRfZ3VpZCI6IjNkOTc0NmQ2MzczZjQyZjc4MzQ3ZTlkNDUzZmZhODY2IiwiY2xpZW50X25hbWUiOiJIYWNrYXRob25PSUNDbGllbnQiLCJ0ZW5hbnRfaXNzIjoiaHR0cHM6XC9cL2lkY3MtNWNkMGM0YTU5M2JiNGE1ODk2NDMzNjdlN2NlMWRkN2UuaWRlbnRpdHkub3JhY2xlY2xvdWQuY29tOjQ0MyIsInRlbmFudCI6ImlkY3MtNWNkMGM0YTU5M2JiNGE1ODk2NDMzNjdlN2NlMWRkN2UiLCJqdGkiOiJjNmRlYWMyNTQ5OWQ0ZTYzYTM3MzcxNjQ3YzA4ZjdkNiIsInJlc291cmNlX2FwcF9pZCI6IjYyMWIxNWE4MTg5NjQ0MTJiMDVlZjk0M2I5YjllYTc4In0.ABIMdHyXSTi1sbgFWtzQL-1ND4z4Iyv_h5LsaxhWnopZKbMfdSb2LR_nKuzIp5p2KTeYkwnyzJiTPIC8R1PwSJg-PTZU9eH940Ztz7QtQL1vDnXymR0Tj2mUjM9Ak0ngRYik2UlT0c7I0BvnFVKxUw51LvgQqaKxSrfyR8DN378OHI_oYRDJYFa9LppCknl-giYnp0nZibF2-qUN-wGZ7fGqVc52V0C0o8ZfV2bgBDeMkhVf-KGwaUeAJbc7RqPQ4YYTPYGXo24csG6BBrbKrYyCCPzxdxNGEiTe9yJclfPz_qV5OmSZxeHNpDA0KdsCM-PcuTpvyRkfZwEv7E4EYA'

header = {
    'Authorization': 'Bearer ' + auth,
    'accept': 'application/json'
}

app = FastAPI(
    title="RIGAQI TEAM API",
    description="Mario , Michael, Katon and I created this API to get the data from the RIGAQI team. (created by machine)",
    version="0.0.1",
    terms_of_service="http://canuseethemeta?fuckoff.com/terms/",
    contact={
        "name": "RIGAQI???",
        "url": "http://komarr007.github.io/RIGAQI",
        "email": "mariorangga000@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"compute": "one code per bit"}

@app.get("/data")
async def get_data(account_number:str):
    response = requests.get(URL + account_number, headers=header)
    data = response.json()
    if response.status_code == 200:
        data["status"] = "unpaid"
        return [data]
    else:
        return {"error": "account number not found"}

# @app.post("/record"):
# async def create_record(record: **Record):
#     pass

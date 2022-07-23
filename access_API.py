import requests
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import datetime

pamjaya_auth_url = "https://apigw.withoracle.cloud/pamjaya/token"
client_id = "8d69ec5f0d6c4c72bb03632aaaf9c062"
client_secret = "d8d33ddf-5337-44fc-8d0f-30e721e74a0e"
scope = "https://A8BD01119B22473B93CBABF0046DE054.integration.ocp.oraclecloud.com:443urn:opc:resource:consumer::all"
grant_type = "client_credentials"

data = {
    "grant_type": grant_type,
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": scope
}

auth = requests.post(pamjaya_auth_url, data=data)
auth_response_json = auth.json()
auth_token = auth_response_json["access_token"]

URL = "https://apigw.withoracle.cloud/pamjaya/beta/account/"

header = {
    'Authorization': 'Bearer ' + auth_token,
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

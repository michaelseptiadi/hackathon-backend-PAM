import requests
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datetime
import os


pamjaya_auth_url = "https://apigw.withoracle.cloud/pamjaya/token"
client_id = "8d69ec5f0d6c4c72bb03632aaaf9c062"
client_secret = "d8d33ddf-5337-44fc-8d0f-30e721e74a0e"
scope = "https://A8BD01119B22473B93CBABF0046DE054.integration.ocp.oraclecloud.com:443urn:opc:resource:consumer::all"
grant_type = "client_credentials"

def get_token(client_id, client_secret, scope, grant_type):
    data = {
        "grant_type": grant_type,
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": scope
    }

    auth = requests.post(
        pamjaya_auth_url, 
        data=data
    )
    auth_response_json = auth.json()
    auth_token = auth_response_json["access_token"]
    return auth_token

URL_PAYMENT = "https://apigw.withoracle.cloud/pamjaya/payment/pay/"
URL_CHARGE = "https://apigw.withoracle.cloud/pamjaya/payment/charge/"
URL_BALANCE = "https://apigw.withoracle.cloud/pamjaya/payment/balance/"
URL_BETA = "https://apigw.withoracle.cloud/pamjaya/account/"

header = {
    'Authorization': 'Bearer ' + get_token(
        client_id, client_secret, scope, grant_type
    ),
    'accept': 'application/json'
}

app = FastAPI(
    title="RIGAQI TEAM API",
    description="Mario , Michael, Katon created this API to get the data from the RIGAQI team. (created by machine)",
    version="0.0.1",
    terms_of_service="",
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

def generate_report(json_data, report_data):
    file_name = "report - " + json_data["account_number"] + "-" + datetime.datetime.now().strftime("%Y") + ".json"
    
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    if file_name not in files:
        with open(file_name, 'w') as outfile:
            outfile.write(json.dumps(report_data))
    elif file_name in files:
        json_data = json.load(open(file_name))
        json_data["data"].append(report_data["data"][0])
        new_data = {
            "account_number": json_data["account_number"],
            "data": json_data["data"]
        }
        with open(file_name, 'w') as outfile:
            outfile.write(json.dumps(new_data))


@app.get("/")
async def root():
    return {"compute": "one code per bit"}

@app.post("/pay")
async def payment(account_number:str, amount:int):
    json_data = {
        "account_number": account_number,
        "amount": amount,
        "payment_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    response = requests.post(
        URL_PAYMENT,
        json = json_data, 
        headers=header
    )
    report_data = {
        "account_number": json_data["account_number"],
        "data" : [
            {
                "tahun" : datetime.datetime.now().strftime("%Y"),
                "bulan" : datetime.datetime.now().strftime("%m"),
                "tipe_transaksi" : "Pembayaran",
                "jumlah_bayar" : amount,
                "volume" : "3000 ML"
            }
        ]
    }
    generate_report(
        json_data, 
        report_data
    )
    data = response.json()
    return [data]

@app.post("/charge")
async def charge(account_number:str, amount:int):
    json_data = {
        "account_number": account_number,
        "amount": amount
    }
    response = requests.post(
        URL_CHARGE,
        json = json_data,
        headers=header
    )
    report_data = {
        "account_number": json_data["account_number"],
        "data" : [
            {
                "tahun" : datetime.datetime.now().strftime("%Y"),
                "bulan" : datetime.datetime.now().strftime("%m"),
                "tipe_transaksi" : "Isi Saldo",
                "jumlah_bayar" : amount,
                "volume" : None
            }
        ]
    }
    generate_report(
        json_data, 
        report_data
    )
    data = response.json()
    return [data]

@app.get("/balance")
async def balance(account_number:str):
    json_data = {
        "account_number": account_number
    }
    response = requests.get(
        URL_BALANCE + json_data["account_number"],
        headers=header
    )
    data = response.json()
    return [data]

@app.get("/beta")
async def beta(account_number:str):
    json_data = {
        "account_number": account_number
    }
    response = requests.get(
        URL_BETA + json_data["account_number"],
        headers=header
    )
    if response.status_code == 200:
        data = response.json()
        data["status"] = "unpaid"
        return [data]
    else:
        return {"error": "account number not found"}

@app.get("/report")
async def report(account_number:str):
    json_account_number = {
        "account_number": account_number
    }
    json_data = json.load(open("report - " + json_account_number["account_number"] + "-" + datetime.datetime.now().strftime("%Y") + ".json"))
    if json_account_number["account_number"] == json_account_number["account_number"]:
        return [json_data]

# @app.post("/record"):
# async def create_record(record: **Record):
#     pass
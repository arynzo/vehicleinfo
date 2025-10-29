from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/vehicle/{vehicle_number}")
def get_vehicle_info(vehicle_number: str):
    url = "https://rtovehicleinfo.com/new_project/api/vehicle-info"
    data = f'{{"vehicleId":"{vehicle_number}"}}'

    headers = {
        "Content-Type": "application/json",
        "x-api-key": "f70cc0cc33617d1903db6c69d008db1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 Chrome/129.0 Mobile Safari/537.36",
        "Host": "rtovehicleinfo.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "Content-Length": str(len(data))
    }

    try:
        res = requests.post(url, headers=headers, data=data)
        return res.json()  # JSON response return karega
    except Exception as e:
        return {"error": str(e)}

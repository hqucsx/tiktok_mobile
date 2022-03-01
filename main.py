from fastapi import FastAPI
from models import DeviceRegisterRequest
from api.device_register import DeviceRegister
import uvicorn
import os
app = FastAPI()


@app.post("/")
def device_register(request: DeviceRegisterRequest):
    gorgon_signer = request.gorgon_signer

    if gorgon_signer is None:
        return {
            "Error" : "Gorgon signer can not be empty"
        }
         
    api = DeviceRegister(gorgon_signer=gorgon_signer,  proxy=request.proxy)

    device, cookies =  api.device_register()

    if device is None or cookies is None:
        response = {
            "Error" : "Switch proxy"
        }
        return response

    response = {
        'device': device.__dict__,
        'cookies' : cookies
    }
    return response


if __name__ == '__main__':
    uvicorn.run(app, port=os.environ.get('APP_PORT'), host='0.0.0.0')

from pydantic import BaseModel


class DeviceRegisterRequest(BaseModel):
    gorgon_signer : str = None
    proxy : str = None
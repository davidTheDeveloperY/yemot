from .client import Client

class IVR:
    def __init__(self, client: Client):
        self.client = client

    def ivr_info(self):
        return self.client.get("GetIVR")
    
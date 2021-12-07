import requests


class Yemot():

    username = None
    password = None
    base_url = None
    token = None

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username=None, password=None):
        if username != None:
            self.username = username
        if password != None:
            self.password = password
        for sub in ["www", "private"]:
            url = f"https://{sub}.call2all.co.il/ym/api/Login?username={self.username}&password={self.password}"
            r = requests.get(url)
            if 'token' in r.json():
                self.token = r.json()['token']
                self.base_url = f"https://{sub}.call2all.co.il/ym/api/"
                return r.json()["responseStatus"]
                break
        if self.token == None:
            return 'username or password is incorrect'

    def logout(self):
        web_service = "Logout"
        r = requests.get(f"{self.base_url}{web_service}/?token={self.token}")
        return r.json()['message']

    def system_info(self):
        web_service = "GetSession"
        r = requests.get(f"{self.base_url}{web_service}/?token={self.token}")
        if 'message' in r.json():
            self.login()
            r = requests.get(
                f"{self.base_url}{web_service}/?token={self.token}")
        return r.json()

import requests
import json


class Yemot():

    username = None
    password = None
    base_url = None
    token = None

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login()

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
        if self.base_url == None:
            self.login()
        web_service = "Logout"
        r = requests.get(f"{self.base_url}{web_service}/?token={self.token}")
        self.base_url = None
        self.username = None
        self.password = None
        self.token = None
        return r.json()['message']

    def system_info(self):
        if self.base_url == None:
            self.login()
        web_service = "GetSession"
        r = requests.get(f"{self.base_url}{web_service}/?token={self.token}")
        if 'message' in r.json():
            self.login()
            r = requests.get(
                f"{self.base_url}{web_service}/?token={self.token}")
        res = {}
        for item in r.json():
            if item != 'responseStatus' and item != 'yemotAPIVersion':
                res[item] = r.json()[item]
        return res

    def set_system_info(self, name=None, email=None, organization=None, contact_name=None, phones=None, invoice_name=None, invoice_address=None, fax=None, access_password=None, record_password=None):
        if self.base_url == None:
            self.login()
        web_service = 'SetCustomerDetails'
        data = {}
        for i, item in [["name", name], ["email", email], ["organization", organization], ["contactName", contact_name], ["phones", phones], ["invoiceName", invoice_name], ["invoiceAddress", invoice_address], ["fax", fax], ["accessPassword", access_password], ["recordPassword", record_password]]:
            if item != None:
                data[i] = item

        r = requests.post(
            f"{self.base_url}{web_service}/?token={self.token}", data=data)
        if r.json()['message'] != 'ok':
            self.login()
            r = requests.post(
                f"{self.base_url}{web_service}/?token={self.token}", data=data)
        new = self.system_info()
        return new

    def set_password(self, new_password):
        if self.base_url == None:
            self.login()
        web_service = 'SetPassword'
        r = requests.get(
            f"{self.base_url}{web_service}/?token={self.token}&password={self.password}&newPassword={new_password}")
        if r.json()['message'] == 'ok':
            self.password = new_password
            return f'Password set the new passwordis{new_password}'
        if r.json()['message'] != 'ok':
            self.login()
            r = requests.get(
                f"{self.base_url}{web_service}/?token={self.token}&password={self.password}&newPassword={new_password}")
            if r.json()['message'] == 'ok':
                self.password = new_password
                return f'Password set, the new password is : {new_password}'

    def get_units_transactions(self, first=None, limit='100'):
        if self.base_url == None:
            self.login()
        web_service = 'GetTransactions'
        data = ''
        if first != None:
            data += f"&from={first}"
        if limit != None:
            data += f"&limit={limit}"
        r = requests.get(
            f"{self.base_url}{web_service}/?token={self.token}{data}")
        if 'message' in r.json():
            self.login()
            r = requests.get(
                f"{self.base_url}{web_service}/?token={self.token}{data}")
        res = {}
        for item in r.json():
            if item != 'responseStatus' and item != 'yemotAPIVersion':
                res[item] = r.json()[item]
        return res

    def transfer_units(self, destination=None, amount=None):
        if destination == None and amount == None:
            return "Destination and amount cannot be empty"
        try:
            int(destination)
            int(amount)
        except:
            return "destination and amount must be a number"
        if self.base_url == None:
            self.login()
        web_service = 'TransferUnits'
        r = requests.get(
            f"{self.base_url}{web_service}/?token={self.token}&destination={destination}&amount={amount}")
        if 'message' in r.json():
            if 'messageCode' in r.json():
                code = {'111': 'Bad destination',
                        '112': 'Bad amount', '113': 'Not enough balance'}
                return code[r.json()['messageCode']]
            else:
                self.login()
                r = requests.get(
                    f"{self.base_url}{web_service}/?token={self.token}&destination={destination}&amount={amount}")
                if 'messageCode' in r.json():
                    code = {'111': 'Bad destination',
                            '112': 'Bad amount', '113': 'Not enough balance'}
                    return code[r.json()['messageCode']]

        res = {}
        for item in r.json():
            if item != 'responseStatus' and item != 'yemotAPIVersion':
                res[item] = r.json()[item]
        return res

    def incoming_calls(self):
        if self.base_url == None:
            self.login()
        web_service = 'GetIncomingCalls'
        r = requests.get(
            f"{self.base_url}{web_service}/?token={self.token}")
        if 'message' in r.json():
            self.login()
            r = requests.get(
                f"{self.base_url}{web_service}/?token={self.token}")
        res = {}
        for item in r.json():
            if item != 'responseStatus' and item != 'yemotAPIVersion':
                res[item] = r.json()[item]
        return res

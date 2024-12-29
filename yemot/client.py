import requests

class Client:
    """
    connect to the yemot
    """
    def __init__(self, username: str, password: str):
        """
        connect to the yemot with the username and password

        Parameters
        ----------
        username : string
            the phone number of the yemot account
        password : string
            password of the yemot account probably its 6 digits
        """
        self.username = username
        self.password = password
        self.token = None
        self.base_url = "https://www.call2all.co.il/ym/api/"
        self.login()

    
    def __str__(self):
        """
        return the token if it exists

        Returns
        -------
        string
            the token if it exists
        """
        return self.token

    
    def __repr__(self):
        """
        return the token if it exists

        Returns
        -------
        string
            the token if it exists
        """
        return self.token
    
    def __del__(self):
        """
        logout from the yemot and delete the token
        """
        self.logout()

    
    def __enter__(self):
        """
        
        establish a connection to the yemot
        """
        self.connected = True
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """
        logout from the yemot and delete the token
        """
        self.logout()
        self.connected = False
        print('connection closed')
        if exc_type:
            print(f'An exception accured: {exc_type}, {exc_value}')
        return True


    def login(self, username=None, password=None):
        """
        reconnect to the yemot with the username and password or regenerate the token if the token is expired

        Parameters
        ----------
        username : string, optional
            the phone number of the yemot account, by default None
        password : string, optional
            password of the yemot account probably its 6 digits, by default None

        Returns
        -------
        string
            the response status or the message if the username or password is incorrect
        """
        if username != None:
            self.username = username
        if password != None:
            self.password = password
        url = f"https://www.call2all.co.il/ym/api/Login?username={self.username}&password={self.password}"
        r = requests.get(url)
        if 'token' in r.json():
            self.token = r.json()['token']
            return r.json()["responseStatus"]
        if self.token == None:
            return 'username or password is incorrect'
        
    def logout(self):
        """
        logout from the yemot and delete the token

        Returns
        -------
        string
            the response message of loging out
        """
        web_service = "Logout"
        r = requests.get(f"https://www.call2all.co.il/ym/api/{web_service}/?token={self.token}")
        return r.json()['message']
    
    def get(self, web_service, params=None):
        """
        a template for get request to the yemot

        Parameters
        ----------
        web_service : string
            the web service name
        params : additinal parameters, optional
            the additional parameters, by default None

        Returns
        -------
        json
            the response of the request
        """
        if self.token == None:
            self.login()
        r = requests.get(f"{self.base_url}{web_service}/?token={self.token}", params=params)
        if 'message' in r.json():
            self.login()
            r = requests.get(f"{self.base_url}{web_service}/?token={self.token}", params=params)
        return r.json()
    
    def post(self, web_service, data=None):
        """
        a template for post request to the yemot

        Parameters
        ----------
        web_service : string
            the web service name
        data : dict, optional
            the data to post, by default None

        Returns
        -------
        json
            the response of the request
        """
        if self.token == None:
            self.login()
        r = requests.post(f"{self.base_url}{web_service}/?token={self.token}", data=data)
        if 'message' in r.json():
            self.login()
            r = requests.post(f"{self.base_url}{web_service}/?token={self.token}", data=data)
        return r.json()
    
    def post_file(self, web_service, file, data=None):
        """
        a template for post request to the yemot with file

        Parameters
        ----------
        web_service : string
            the web service name
        file : string
            the file path
        data : dict, optional
            the data to post, by default None

        Returns
        -------
        json
            the response of the request
        """
        if self.token is None:
            self.login()

        with open(file, 'rb') as f:
            r = requests.post(
                f"{self.base_url}{web_service}/?token={self.token}",
                files={'file': f},
                headers={'Content-Type': 'multipart/form-data'},
                data=data
            )

        if 'message' in r.json():
            self.login()
            with open(file, 'rb') as f:
                r = requests.post(
                    f"{self.base_url}{web_service}/?token={self.token}",
                    files={'file': f},
                    headers={'Content-Type': 'multipart/form-data'},
                    data=data
                )
        return r.json()
    
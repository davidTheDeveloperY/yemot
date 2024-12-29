from .client import Client

class System:
    """
    Get the system information and set the system information
    """
    def __init__(self, client: Client):
        self.client = client

    def system_info(self):
        """
        Get the system information

        Returns
        -------
        json
            the system information
        """
        return self.client.get("GetSession")
    
    def set_system_info(self, name=None, email=None, organization=None, contact_name=None, phones=None, invoice_name=None, invoice_address=None, fax=None, access_password=None, record_password=None):
        """
        Set the system information you can set some of the parameters or all of them to set the system information

        Parameters
        ----------
        name : string, optional
            the name of the user, by default None
        email : string, optional
            the users email, by default None
        organization : string, optional
            the name of your organiztion, by default None
        contact_name : string, optional
            the contact user, by default None
        phones : string, optional
            the users phone, by default None
        invoice_name : string, optional
            the name for the invoice, by default None
        invoice_address : string, optional
            the email for the invoice, by default None
        fax : string, optional
            the fax number, by default None
        access_password : string, optional
            the main password, by default None
        record_password : string, optional
            the password for limited access, by default None

        Returns
        -------
        json
            the new system information
        """
        data = {
            "name": name,
            "email": email,
            "organization": organization,
            "contactName": contact_name,
            "phones": phones,
            "invoiceName": invoice_name,
            "invoiceAddress": invoice_address,
            "fax": fax,
            "accessPassword": access_password,
            "recordPassword": record_password
        }
        return self.client.post("SetCustomerDetails", data)
    
    def set_password(self, new_password):
        """
        Set the new password

        Parameters
        ----------
        new_password : string
            the new password

        Returns
        -------
        json
            the new password
        """
        if not isinstance(new_password, int):
            return "The password must be a integer"
        new = self.client.get("SetPassword", {"password": self.client.password, "newPassword": new_password})
        self.client.password = new_password
        return new
    
    def get_transactions(self, first=None, limit='100', filter=None):
        """
        Get the transactions of the units in the system

        Parameters
        ----------
        first : string, optional
            the number to start, by default None
        limit : str, optional
            how meny to show, by default '100'
        filter : string, optional
            the filter for example: "campaigns", by default None

        Returns
        -------
        json
            the transactions of the units
        """
        return self.client.get("GetTransactions", {"first": first, "limit": limit})
    
    def transfer_units(self, amount, destination):
        """
        Transfer units to another account

        Parameters
        ----------
        amount : int
            the amount of units
        destination : string
            the destination account

        Returns
        -------
        json
            the response of the transfer
        """
        if not isinstance(amount, int):
            return "The amount must be a integer"
        if not isinstance(destination, int):
            return "The destination must be a integer"
        return self.client.get("TransferUnits", {"amount": amount, "destination": destination})
    
    def get_incoming_calls(self):
        """
        Get the incoming calls

        Returns
        -------
        json
            the incoming calls
        """
        return self.client.get("GetIncomingCalls")
    
    def upload_file(self, file, path, convert_audio=0, auto_numbering=False, tts=0):
        """
        Upload file to the system

        Parameters
        ----------
        file : string
            the path to the file to upload,
        path : string
            the path where will the file saved its need to start with ivr2: and includeing the name if not using the auto numbering
        convert_audio : int, optional
            if it a audio file not in the wav format convert it, by default 0
        auto_numbering : bool, optional
            if true save the file with a auto numbering name, by default False
        tts : int, optional
            its used if auto numbering is true, by default 0

        Returns
        -------
        json
            the response of the upload
        """
        if not file:
            return "The file is required"
        # check if the path starts with ivr2:
        if path and not path.startswith("ivr2:"):
            return "The path must start with ivr2:"
        if convert_audio not in [0, 1]:
            return "The convert_audio must be 0 or 1"
        if tts not in [0, 1]:
            return "The tts must be 0 or 1"
        if auto_numbering not in [True, False]:
            return "The auto_numbering must be True or False"
        
        data = {
            "path": path,
            "convertAudio": convert_audio,
            "autoNumbering": auto_numbering,
            "tts": tts
        }
        return self.client.post_file("UploadFile", data=data, file=file)
    
    def upload_file_big(self, file, path, convert_audio=None, auto_numbering=None, tts=None):
        """
        Upload file this is for uploading a file what is over 50MB not redy yet
        """
        # TODO: Implement this method

        # split the file to parts and upload each part in the first part generate a qquuid and send it to the server
        # the parameter what i need to send in each part is 
        # qquuid - the generated qquuid
        # qqpartindex - the part index
        # qqpartbyteoffset - the part byte offset
        # qqchunksize - the chunk size
        # qqtotalparts - the total parts
        # qqtotalfilesize - the total file size in bytes
        # qqfilename - the file name
        # qqfile - the file
        # uploader - yemot-admin
        return "Not implemented"
    
    def download_file(self, path):
        """
        Download file from the system

        Parameters
        ----------
        path : string
            the path to the file in the system starting with ivr2:

        Returns
        -------
        json
            the response of the download
        """
        if not path:
            return "The path is required"
        return self.client.get("DownloadFile", {"path": path})   
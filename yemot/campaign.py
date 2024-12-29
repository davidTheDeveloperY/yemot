from .client import Client

class Campaign:
    """
    Get the campaign information and set the campaign information
    """
    def __init__(self, client: Client):
        self.client = client

    def get_templates(self):
        """
        Get the templates

        Returns
        -------
        json
            the templates
        """
        return self.client.get("GetTemplates")
    
    def update_template(
            self, template_id,
            description: str=None,
            caller_id: str=None,
            incoming_policy: str=None,
            customer_default: str=None,
            max_acive_channels: int=None,
            max_bridged_channels: int=None,
            originate_timeout: int=None,
            vm_detect: str=None,
            filter_enabled: str=None,
            max_dail_attempts: int=None,
            redial_wait: int=None,
            redail_policy: str=None,
            yemot_context: str=None,
            bridge_to: str=None,
            play_private_msg: str=None,
            remove_request: str=None):
        """
        Update a telephony template with given parameters.

        Parameters
        ----------
        template_id : int
            ID of the template to update
        description : str, optional
            Description of the template
        caller_id : str, optional
            Caller ID associated with this template
        incoming_policy : str, optional
            Incoming policy, one of: 'OPEN', 'BLACKLIST', 'WHITELIST', 'BLOCKED'
        customer_default : str, optional
            Whether this template is the default for the customer, '0' or '1'
        max_active_channels : int, optional
            The maximum active channels allowed
        max_bridged_channels : int, optional
            The maximum bridged channels allowed
        originate_timeout : int, optional
            Timeout (in seconds) when originating a call
        vm_detect : str, optional
            Voicemail detection enabled, '0' or '1'
        filter_enabled : str, optional
            Whether filtering is enabled, '0' or '1'
        max_dial_attempts : int, optional
            Maximum dial attempts
        redial_wait : int, optional
            How many seconds to wait before redialing
        redial_policy : str, optional
            Redial policy, one of: 'NONE', 'CONGESTIONS', 'FAILED'
        yemot_context : str, optional
            YEMOT context, one of: 'SIMPLE', 'REPEAT', 'MESSAGE', 'VOICEMAIL', 'BRIDGE'
        bridge_to : int, optional
            ID to bridge calls to
        play_private_msg : str, optional
            Whether to play a private message, '0' or '1'
        remove_request : str, optional
            Removal request type, 'SILENT' or 'WITH_MESSAGE'

        Returns
        -------
        Any
            Response from the client post request
        """
        
        if not isinstance(template_id, int):
            return "The template_id must be a integer"
        
        if incoming_policy not in [None, 'OPEN', 'BLACKLIST', 'WHITELIST', 'BLOCKED']:
            return "The incoming_policy must be one of the following: 'OPEN', 'BLACKLIST', 'WHITELIST', 'BLOCKED'"
        
        if customer_default not in [None, '0', '1']:
            return "The customer_default must be one of the following: '0', '1'"
        
        if max_acive_channels and not isinstance(max_acive_channels, int):
            return "The max_acive_channels must be a integer"
        
        if max_bridged_channels and not isinstance(max_bridged_channels, int):
            return "The max_bridged_channels must be a integer"
        
        if originate_timeout and not isinstance(originate_timeout, int):
            return "The originate_timeout must be a integer"
        
        if vm_detect not in [None, '0', '1']:
            return "The vm_detect must be one of the following: '0', '1'"
        
        if filter_enabled not in [None, '0', '1']:
            return "The filter_enabled must be one of the following: '0', '1'"
        
        if max_dail_attempts and not isinstance(max_dail_attempts, int):
            return "The max_dail_attempts must be a integer"
        
        if redial_wait and not isinstance(redial_wait, int):
            return "The redial_wait must be a integer"
        
        if redail_policy not in [None, 'NONE', 'CONGESTIONS', 'FAILED']:
            return "The redail_policy must be one of the following: 'NONE', 'CONGESTIONS', 'FAILED'"
        
        if yemot_context not in [None, 'SIMPLE', 'REPEAT', 'MESSAGE', 'VOICEMAIL', 'BRIDGE']:
            return "The yemot_context must be one of the following: 'SIMPLE', 'REPEAT', 'MESSAGE', 'VOICEMAIL', 'BRIDGE'"
        
        if bridge_to and not isinstance(bridge_to, int):
            return "The bridge_to must be a integer"
        
        if play_private_msg not in [None, '0', '1']:
            return "The play_private_msg must be one of the following: '0', '1'"
        
        if remove_request not in [None, 'SILENT', 'WITH_MESSAGE']:
            return "The remove_request must be one of the following: 'SILENT', 'WITH_MESSAGE'"
        
        data = {
            "templateId": template_id,
            "description": description,
            "callerId": caller_id,
            "incomingPolicy": incoming_policy,
            "customerDefault": customer_default,
            "maxActiveChannels": max_acive_channels,
            "maxBridgedChannels": max_bridged_channels,
            "originateTimeout": originate_timeout,
            "vmDetect": vm_detect,
            "filterEnabled": filter_enabled,
            "maxDailAttempts": max_dail_attempts,
            "redialWait": redial_wait,
            "redailPolicy": redail_policy,
            "yemotContext": yemot_context,
            "bridgeTo": bridge_to,
            "playPrivateMsg": play_private_msg,
            "removeRequest": remove_request
        }
        return self.client.post("UpdateTemplate", data=data)
    
    def upload_template_file(self, file: str, name: str, type: str, convertAudio: str=None):
        """
        Upload the template file

        Parameters
        ----------
        file : string
            the path to the file to upload
        name : string, optional
            the name of the file the template id or the phone number if using the PRIVATE_MSG type, by default None
        type : string
            the type of the file, one of: 'VOICE', 'SMS', 'BRIDGE' - for a msg befor bridge, 'PRIVATE_FIRST', 'PRIVATE_MSG'
        convertAudio : int, optional
            0 or 1 if the file is not in the wav format, by default None

        Returns
        -------
        json
            the response of the upload
        """
        if name == None:
            name = "Default"
        if type not in ['VOICE', 'SMS', 'BRIDGE', 'PRIVATE_FIRST', 'PRIVATE_MSG']:
            return "The type must be one of the following: 'VOICE', 'SMS', 'BRIDGE' - for a msg befor bridge, 'PRIVATE_FIRST', 'PRIVATE_MSG'"
        
        if not file:
            return "The file is required"
        
        if type == 'VOICE':
            path = f'{name}.wav'
        if type == 'SMS':
            path = f'{name}.tts'
        if type == 'BRIDGE':
            path = f'{name}-MoreInfo.wav'
        if type == 'PRIVATE_FIRST':
            path = f'{name}-First.wav'
        if type == 'PRIVATE_MSG':
            path = f'PrivateMsg/{name}.wav'
        
        return self.client.post_file("UploadFile", data={"path": path, "convertAudio": convertAudio}, file=file)
    
    def downlaoad_template_file(self, name: str, type: str):
        """
        Download the template file

        Parameters
        ----------
        name : string, optional
            the name of the file the template id or the phone number if using the PRIVATE_MSG type, by default None
        type : string
            the type of the file, one of: 'VOICE', 'SMS', 'BRIDGE' - for a msg befor bridge, 'PRIVATE_FIRST', 'PRIVATE_MSG'

        Returns
        -------
        json
            the response of the download
        """
        if name == None:
            name = "Default"
        if type not in ['VOICE', 'SMS', 'BRIDGE', 'PRIVATE_FIRST', 'PRIVATE_MSG']:
            return "The type must be one of the following: 'VOICE', 'SMS', 'BRIDGE' - for a msg befor bridge, 'PRIVATE_FIRST', 'PRIVATE_MSG'"
        
        if type == 'VOICE':
            path = f'{name}.wav'
        if type == 'SMS':
            path = f'{name}.tts'
        if type == 'BRIDGE':
            path = f'{name}-MoreInfo.wav'
        if type == 'PRIVATE_FIRST':
            path = f'{name}-First.wav'
        if type == 'PRIVATE_MSG':
            path = f'PrivateMsg/{name}.wav'
        
        return self.client.get("DownloadFile", {"path": path})
    
    # TODO: Implement the FileAction method and GetTextFile method and UploadTextFile method

    def create_template(self, description: str):
        """
        Create a new template the details of the template will be generated from the default template to change the details use the update_template method

        Parameters
        ----------
        description : string
            the description of the template

        Returns
        -------
        int
            the template id
        """
        
        return self.client.get("CreateTemplate", {"description": description})
    
    def delete_template(self, template_id: int):
        """
        Delete the template by the template id

        Parameters
        ----------
        template_id : int
            the template id

        Returns
        -------
        json
            success message
        """
        if not isinstance(template_id, int):
            return "The template_id must be a integer"
        
        return self.client.get("DeleteTemplate", {"templateId": template_id})
    
    def get_template_entries(self, template_id: int):
        """
        Get the template entries

        Parameters
        ----------
        template_id : int
            the template id

        Returns
        -------
        json
            the template entries
        """
        if not isinstance(template_id, int):
            return "The template_id must be a integer"
        
        return self.client.get("GetTemplateEntries", {"templateId": template_id})
    
    def update_template_entry(self, template_id: int, rowid: int=None, phone: str=None, name: str=None, more_info: str=None, blocked: str=0):
        """
        Update a template entry or create a new one

        Parameters
        ----------
        template_id : int
            the template id
        rowid : int, optional
            if not given or not fund will crate a new entry, by default None
        phone : string, optional
            the entry phone, by default None
        name : string, optional
            the name, by default None
        more_info : string, optional
            mor details, by default None
        blocked : int, optional
            to add the user in blcked list, by default 0

        Returns
        -------
        json
            the response of the request
        """
        if not isinstance(template_id, int):
            return "The template_id must be a integer"
        
        if rowid and not isinstance(rowid, int):
            return "The rowid must be a integer"
        
        if blocked not in [0, 1]:
            return "The blocked must be 0 or 1"
        
        data = {
            "templateId": template_id,
            "rowid": rowid,
            "phone": phone,
            "name": name,
            "moreInfo": more_info,
            "blocked": blocked
        }
        return self.client.post("UpdateTemplateEntry", data=data)
    


        
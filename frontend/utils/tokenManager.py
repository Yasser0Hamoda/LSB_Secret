import keyring

class TokenManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TokenManager, cls).__new__(cls)
            cls._instance.access_token = None
            cls._instance.refresh_token = None
            cls._instance.remember_me = False
        return cls._instance
    
    def set_access_token(self, access_token:str):
        self.access_token = access_token
    
    def set_tokens(self, access_token:str, refresh_token:str, rememberMe:bool):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.remember_me=rememberMe
        
        if rememberMe:
            keyring.set_password('stegano_app','refresh_token', refresh_token)
        else:
            try:
                keyring.delete_password('stegano_app', 'refresh_token')
            except:
                pass
            
    def load_Stored_Refresh_Token(self):
        token=keyring.get_password('stegano_app', 'refresh_token')
        
        if token is not None:
            self.refresh_token = token
            self.remember_me = True
            return token
        else:
            return None
        
    def clear(self):
        self.access_token=None
        self.refresh_token=None
        self.remember_me=False
        
        try:
            keyring.delete_password('stegano_app', 'refresh_token')
        except:
            pass
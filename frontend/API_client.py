import requests
from utils.helper import helper
from config import REGISTER_ENDPOINT_URL, LOGIN_ENDPOINT_URL

class API_client:
    
    @staticmethod
    def signUp(user_name:str, password:str, pass_confirm:str)->dict:
        if not helper.there_is_internet_connection():
            return helper.makeFailureResponse('There is internet connection!')
        
        data = {
            'user_name':user_name,
            'password': password,
            'pass_confirm':pass_confirm
        }
        
        try:
            response = requests.post(url=REGISTER_ENDPOINT_URL, data=data)
            return dict(response.json())  
        except requests.RequestException as e:
            return helper.makeFailureResponse(e)

    @staticmethod
    def login(user_name:str, password:str)->dict:
        if not helper.there_is_internet_connection():
            return helper.makeFailureResponse('There is internet connection!')
        
        data = {
            'user_name':user_name,
            'password': password,
        }
        
        try:
            response = requests.post(url=LOGIN_ENDPOINT_URL, data=data)
            return dict(response.json())  
        except requests.RequestException as e:
            return helper.makeFailureResponse(e)

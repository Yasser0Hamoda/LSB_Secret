import requests
import os
from utils.helper import helper
from utils.tokenManager import TokenManager
from config import (REGISTER_ENDPOINT_URL, LOGIN_ENDPOINT_URL, REFRESH_ENDPOINT_URL,
                    EMBED_ENDPOINT_URL, EXTRACT_ENDPOINT_URL, SAVE_MESSAGE_ENDPOINT_URL, GET_ALL_MESSAGES_ENDPOINT_URL)

tm = TokenManager()

class API_client:
    
    @staticmethod
    def signUp(user_name:str, password:str, pass_confirm:str)->dict:
        '''Function to sign up a new user to the system'''
        if not helper.there_is_internet_connection():
            return helper.makeFailureResponse('There is no internet connection!')
        
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
    def login(user_name:str, password:str, rememberMe:bool)->dict:
        '''Function to log in the user to the system'''
        if not helper.there_is_internet_connection():
            return helper.makeFailureResponse('There is no internet connection!')
        
        data = {
            'user_name':user_name,
            'password': password,
        }
        
        try:
            response = dict(requests.post(url=LOGIN_ENDPOINT_URL, data=data).json())
            if response.get('status') == 'fail':
                return response 
            else:
                access_token = response.get('access_token')
                refresh_token = response.get('refresh_token')
                if access_token and refresh_token:
                    tm.set_tokens(access_token, refresh_token, rememberMe)                    
                return {'status':'success'}
        except requests.RequestException as e:
            return helper.makeFailureResponse(e)

    def __refresh():
        '''Function to refresh the access token'''
        headers={
            'Authorization':f'Bearer {tm.refresh_token}'
        }
        
        try:
            response = dict(requests.post(url=REFRESH_ENDPOINT_URL,headers=headers).json())
            status = response.get('status')
            if status == 'success':
                tm.set_access_token(response.get('access_token'))
            return True
        except:
            return False
      
    @staticmethod  
    def embed(message:str, password:str, image_path:str):
        if not helper.there_is_internet_connection():
            return helper.makeFailureResponse('There is no internet connection!')
        
        if not os.path.exists(image_path):
            return helper.makeFailureResponse('Image Does Not Exists!')
        
        data={
            'message':message,
            'password':password,
        }
        with open(image_path,'rb') as image_file:
            files={
                'image':image_file
            }
        headers={
            'Authorization':f'Bearer {tm.access_token}'
        }
        try:
            response = requests.post(url=EMBED_ENDPOINT_URL, files=files, headers=headers, data=data)
            if response.status_code == 401:
                result = API_client.__refresh()
                if not result:
                    return helper.makeFailureResponse('tokens has expired, you have to login again!')
                return API_client.embed(message,password,image_path)
            elif response.status_code != 200:
                return dict(response.json())
            else:
                return response
        except requests.RequestException as e:
            return helper.makeFailureResponse(str(e))

    @staticmethod
    def extract(image_path:str, password:str):
        '''Function to Extract the message from the image'''
        if not helper.there_is_internet_connection():
            return helper.makeFailureResponse('There is no internet connection!')
        
        if not os.path.exists(image_path):
            return helper.makeFailureResponse('Image Does Not Exists!')
        
        data={
            'password':password
        }
        with open(image_path, 'rb') as miage_file:
            files={
                'image':miage_file
            }
        headers={
            'Authorization':f'Bearer {tm.access_token}'
        }
        try:
            response = requests.post(url=EXTRACT_ENDPOINT_URL,data=data, files=files, headers=headers)
            if response.status_code == 401:
                res = API_client.__refresh()
                if not res:
                    return helper.makeFailureResponse('tokens has expired, you have to login again!')
                return API_client.extract(image_path,password)
            return dict(response.json())
        except requests.RequestException as e:
            return helper.makeFailureResponse(str(e))
    
    @staticmethod
    def save_message(message:str):
        if not helper.there_is_internet_connection():
            return helper.makeFailureResponse('There is no internet connection!')
        
        try:
            response = requests.post(url=SAVE_MESSAGE_ENDPOINT_URL,data={'message':str(message)},headers={'Authorization':f'Bearer {tm.access_token}'})
            if response.status_code==401:
                res = API_client.__refresh()
                if not res:
                    return helper.makeFailureResponse('tokens has expired, you have to login again!')
                return API_client.save_message(message)
            return dict(response.json())
        except requests.RequestException as e:
            return helper.makeFailureResponse(str(e))
    
    @staticmethod
    def get_all_messages():
        if not helper.there_is_internet_connection():
            return helper.makeFailureResponse('There is no internet connection!')
        
        try:
            response = requests.get(url=GET_ALL_MESSAGES_ENDPOINT_URL,headers={'Authorization':f'Bearer {tm.access_token}'})
            if response.status_code==401:
                res = API_client.__refresh()
                if not res:
                    return helper.makeFailureResponse('tokens has expired, you have to login again!')
                return API_client.get_all_messages()
            return dict(response.json())
        except requests.RequestException as e:
            return helper.makeFailureResponse(str(e))
        
            

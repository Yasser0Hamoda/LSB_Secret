import requests

class helper:
    
    @staticmethod
    def there_is_internet_connection()->bool:
        '''
            function to check whether there is internet connection or not
        '''
        try:
            requests.get("https://www.google.com", timeout=3)
            return True
        except requests.RequestException:
            return False

    @staticmethod
    def makeFailureResponse(reason:str)->dict:
        return {
            'status':'fail',
            'reason':str(reason)
        }
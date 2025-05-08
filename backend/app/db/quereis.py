import sqlite3
from .database import get_db_conn
from utils.encryption import crypto

class queries:
    @staticmethod
    def add_user(user_name:str, password:str)->tuple[bool, str]:
        """
        Adds a new user to the USERS table after hashing the password.

        Args:
            username (str): The desired username.
            password (str): The user's plaintext password.

        Returns:
            (bool, str): A tuple (success, message).
        """
        conn=get_db_conn()
        cur=conn.cursor()
        try:
            password = crypto.hash_pass(password)
            cur.execute('INSERT INTO USERS(username, password) VALUES(?,?)', (user_name, password))
            conn.commit()
            return True, 'User regestered Successfully'
        except sqlite3.IntegrityError:
            return False, 'User Already Exist'
        except Exception as e:
            return False, f'An Error Has Accured: {e}'
        finally:
            conn.close()
    
    @staticmethod
    def get_password(user_name:str)->tuple[bool, str]:
        '''
            get the hashed password related to a specific username
            
            Args:
                use_name (str): the desired user you want to get its password
            
            Returns:
                tuble(bool, str): a tuble indicating (success, message or hashed password)
        '''
        conn = get_db_conn()
        cur = conn.cursor()
        
        res = cur.execute("SELECT password FROM USERS WHERE username=?", (user_name,)).fetchall()
        conn.close()
        if not res:
            return False, 'Wrong User Name Or Password'
        else:
            return True, res[0][0]
    
    @staticmethod
    def get_user_id(user_name)->tuple[bool, str]:
        """
        gets user ID from his/her username.

        Args:
            username (str): The desired username.

        Returns:
            (bool, str): A tuple (success, message or userID).
        """
        
        conn = get_db_conn()
        cur = conn.cursor()
        
        res = cur.execute("SELECT user_id FROM USERS WHERE username=?", (user_name,)).fetchall()
        conn.close()
        if not res:
            return False, 'Wrong User Name'
        else:
            return True, res[0][0]

    @staticmethod
    def log_user_action(user_id, action, message, status='fail')->bool:
        """
        Adds the user logs, to the database.

        Args:
            user_id (str): The desired userID.
            action (str): The action that the user is trying to do.
            message (str): detailed explaination of the user's action.
            status (str): indicatnig the success or the failure of the action.

        Returns:
            bool.
        """
        
        conn = get_db_conn()
        cur = conn.cursor()
        try:
            cur.execute('''INSERT INTO logs
                    ('user_id','action','message_snippet','status')
                    VALUES(?,?,?,?);''', (user_id,action, message, status))
            conn.commit()
            return True
        except:
            return False
        finally:
            conn.close()
            

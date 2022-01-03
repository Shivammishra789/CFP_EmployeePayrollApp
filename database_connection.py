'''
@author: Shivam Mishra
@date: 29-12-21 10:43 PM

'''
from mysql.connector import connect, Error
import os
from dotenv import load_dotenv
load_dotenv()


class DBConnection:
    """
    Contains method to establish connection with database
    """
    try:
        @staticmethod
        def establish_connection():
            """
            desc: establish connection with database
            return: connection
            """
            connection = connect(
                host=os.getenv('host'),
                user=os.getenv('user_name'),
                password=os.getenv('password'),
                database='employee'
                )
            return connection
    except Error as ex:
        print(ex)

















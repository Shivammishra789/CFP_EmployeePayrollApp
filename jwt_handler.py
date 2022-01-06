'''
@author: Shivam Mishra
@date: 05-01-22 8:36 PM
'''
import jwt


class JwtHandler:

    @staticmethod
    def encode_token(id):
        """
            desc: this function will encode the payload into a token
            param: id: it is an employee id
            return: token id
        """
        payload = {"user_id": id}
        token_id = jwt.encode(payload, "my_super_secret")
        return token_id

    @staticmethod
    def decode_token(token_id):
        """
            desc: this function will decode the token into a payload
            param: token_id: it is a token which is generated at the time of adding an employee
            return: decoded employee id
        """
        payload = jwt.decode(token_id, "my_super_secret", algorithms=["HS256"])
        return payload.get('user_id')

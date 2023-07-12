import requests
from requests import Response
from ..models.login_credentials_model import login_credentials_model
from requests import session
class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        self.session_headers = headers

    def post_v1_account_login(self, json: login_credentials_model, **kwargs) -> Response:
        """
        Authenticate via credentials
        :param json login_credentials_model
        :return:
        """

        response = self.session.post(
            url=f"{self.host}/v1/account/login",
            json=json,
            **kwargs
        )
        return response

def delete_v1_account_login(self):
    """
    Logout as current user
    :return:
    """

    response = self.session.delete(
        url=f"{self.host}/v1/account/login"
    )
    return response

def delete_v1_account_login_all(self):
    """
    Logout from every device
    :return:
    """

    response = self.session.delete(
        url=f"{self.host}/v1/account/login/all"
    )
    return response

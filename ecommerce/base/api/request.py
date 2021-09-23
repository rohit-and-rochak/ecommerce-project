import requests
from requests.models import HTTPError

from base.models import User


def handle_exception(func):
    def inner_function(*args, **kwargs):
        result = None
        try:
            response = func(*args, **kwargs)
            if response.ok:
                result = response.json()
            else:
                raise HTTPError(response.json())
        except Exception as e:
            print(e)
            result = {"status": "error", "message": str(e)}
        finally:
            return result

    return inner_function


class BaseRequest():
    """
    Helper to call APIs published by other applications
    """

    def __get_anonymous_user_token(self):
        return User.objects.get(username="web-user").get_token()

    @staticmethod
    @handle_exception
    def get(url, token=None):
        token = token or __class__().__get_anonymous_user_token()
        return requests.get(url, headers={"Authorization": "Token {}".format(token)})

    @staticmethod
    @handle_exception
    def post(url, token=None, data=None):
        token = token or __class__().__get_anonymous_user_token()
        return requests.post(url, json=data, headers={"Authorization": "Token {}".format(token)})

    @staticmethod
    @handle_exception
    def patch(url, token=None, data=None):
        token = token or __class__().__get_anonymous_user_token()
        return requests.patch(url, json=data, headers={"Authorization": "Token {}".format(token)})

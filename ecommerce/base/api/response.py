from rest_framework import status
from rest_framework.response import Response


class BaseResponse():
    """
    Common response templates and handlers for API
    Methods are ordered according to HTTP codes
    """

    @staticmethod
    def success(data=None):
        data = {"status": "success", "data": data}

        return Response(status=status.HTTP_200_OK, data=data)

    @staticmethod
    def bad_request(message=None, request=None):
        data = {"status": "bad request", "message": message}

        if request:
            print(request.headers)
            print(request.data)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=data)

    @staticmethod
    def unauthorized(message=None, request=None):
        data = {"status": "unauthorized", "message": message}

        logs = {"message": message}
        if request:
            logs["headers"] = request.headers
            logs["data"] = request.data

        return Response(status=status.HTTP_401_UNAUTHORIZED, data=data)

    @staticmethod
    def error(e, request=None):
        data = {"status": "error", "message": "Internal Server Error"}

        if request:
            print(request.headers)
            print(request.data)

        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data=data)

from exceptions import BaseAPIException

class BaseRequestsException(BaseAPIException):
    def __init__(
        self, *args: object,
        detail: dict = None,
        message: str = 'Something wrong with you requests',
        status_code
    ) -> None:
        super().__init__(*args, detail=detail, message=message, status_code=status_code)

class NoNetworkConnection(BaseRequestsException):
    def __init__(
        self, *args: object,
        detail: dict = None,
        message: str = "Can't connect to host. Internet connection is empty",
        status_code=500
    ) -> None:
        super().__init__(*args, detail=detail, message=message, status_code=status_code)

class RequestedResourceError(BaseRequestsException):
    def __init__(
        self, *args: object,
        detail: dict = None,
        message: str = "Your request was not processed by the resource",
        status_code=500
    ) -> None:
        super().__init__(*args, detail=detail, message=message, status_code=status_code)

class NotFoundError(BaseRequestsException):
    def __init__(
        self, *args: object, 
        message: str = 'Not found url', 
        status_code=404
    ) -> None:
        super().__init__(*args, message=message, status_code=status_code)

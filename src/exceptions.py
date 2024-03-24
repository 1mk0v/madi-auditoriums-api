class BaseAPIException(BaseException):

    def __init__(self, *args: object, detail:dict = None, message:str = 'Base API exception!', status_code) -> None:
        self.detail = detail
        self.message = message
        self.status_code = status_code
        super().__init__(*args)
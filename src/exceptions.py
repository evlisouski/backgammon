from fastapi import HTTPException, status


class Backgammon(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class PointDuplication(Backgammon):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Point numbers must not be duplicated"

class IncorrectNumberOfCheckers(Backgammon):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "The total number of checkers must be between 0-15"

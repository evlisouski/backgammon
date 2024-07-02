import uuid
from enum import Enum
from typing import Dict, List, Optional
from uuid import UUID
from pydantic import BaseModel, Field, field_validator
from typing_extensions import Annotated
from src.exceptions import PointDuplication, IncorrectNumberOfCheckers


class SBoardPoint(BaseModel):
    number: Annotated[int, Field(ge=0, le=23)]
    checkers_count: Annotated[int, Field(ge=0, le=15)]
    occupied_by: Optional[UUID] = None


class SBoard(BaseModel):
    bar_counts: Dict[UUID, Annotated[int, Field(ge=0, le=23)]] = {uuid.uuid4(): 1, }
    points: Annotated[List[SBoardPoint], Field(min_length=24, max_length=24)]


class SGameResultInput(BaseModel):
    board: SBoard
    start_position: Dict[UUID, Annotated[int, Field(ge=0, le=23)]] = {uuid.uuid4(): 1, }

    @field_validator('board')
    def check_duplication_of_point_numbers(cls, board: SBoard):
        point_numbers = [point.number for point in board.points]
        if len(point_numbers) != len(set(point_numbers)):
            raise PointDuplication
        return board

    @field_validator("board")
    def check_incorrect_number_of_checkers(cls, board: SBoard):
        total_checkers = sum(point.checkers_count for point in board.points)
        if total_checkers > 15:
            raise IncorrectNumberOfCheckers
        return board


class GameWinType(str, Enum):
    oin = 'oin'
    mars = 'mars'
    koks = 'koks'


class SGameResultOutput(BaseModel):
    points: Annotated[int, Field(ge=0)]
    win_type: GameWinType

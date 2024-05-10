import uuid
from enum import Enum
from typing import Dict, List, Optional
from uuid import UUID
from pydantic import BaseModel, Field
from typing_extensions import Annotated


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


class GameWinType(str, Enum):
    oin = 'oin'
    mars = 'mars'
    koks = 'koks'


class SGameResultOutput(BaseModel):
    points: Annotated[int, Field(ge=0)]
    win_type: GameWinType

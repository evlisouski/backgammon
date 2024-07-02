from fastapi import APIRouter
from src.score.schemas import SGameResultInput, SGameResultOutput
from src.score.score_calculator import calculate


router = APIRouter(
    prefix="/score",
    tags=["Score"],
)


@router.post("/calculate_score")
async def calculate_score(result_input: SGameResultInput) -> SGameResultOutput:
    result = calculate(result_input)
    return result

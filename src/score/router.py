from fastapi import APIRouter
from src.score.schemas import SGameResultInput, SGameResultOutput
from src.score.score_calculator import calculate
from src.score.additional_validators import checkDuplicationOfPointNumbers, checkIncorrectNumberOfCheckers


router = APIRouter(
    prefix="/score",
    tags=["Score"],
)


@router.post("/calculate_score")
async def calculate_score(result_input: SGameResultInput) -> SGameResultOutput:
    checkDuplicationOfPointNumbers(result_input)
    checkIncorrectNumberOfCheckers(result_input)
    result = calculate(result_input)
    return result

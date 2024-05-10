from src.score.schemas import SGameResultInput
from src.exceptions import PointDuplication, IncorrectNumberOfCheckers


def checkDuplicationOfPointNumbers(result_input: SGameResultInput):
    '''Check that point numbers are not duplicated'''

    mem_list = []
    for i in result_input.board.points:
        if i.number in mem_list:
            raise PointDuplication
        mem_list.append(i.number)


def checkIncorrectNumberOfCheckers(result_input: SGameResultInput):
    '''Check that the total number of checkers on the field is not more than 15'''

    board_map = {int(i.number): int(i.checkers_count)
                 for i in result_input.board.points}
    total_checkers = sum(board_map.values())
    if total_checkers > 15:
        raise IncorrectNumberOfCheckers

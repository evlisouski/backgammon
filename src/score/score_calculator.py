from src.score.schemas import SGameResultInput


def calculate(result_input: SGameResultInput) -> dict:
    """Calculate scores and type of victory in the backgammon short game

    Args:
        result_input (SGameResultInput):
        data structure describing the position of checkers on the field at
        the end of the game. The numbering of the points must be from
        the defeated side.

    Returns:
        Returns a dict with the points and win_type keys
        ex: {"points": 1, "win_type": "oin"}
    """

    result = {"points": 0, "win_type": None}

    # Create a map of the playing field in the form of a dictionary
    board_map = {int(i.number): int(i.checkers_count)
                 for i in result_input.board.points}

    # region Checking conditions for game termination by "koks" type
    player_UUID = list(result_input.board.bar_counts.keys())[0]
    if result_input.board.bar_counts[player_UUID]:
        result["points"] = 3
        result["win_type"] = "koks"
        return result

    for i in range(18, 24):
        if board_map[i]:
            result["points"] = 3
            result["win_type"] = "koks"
            return result
    # endregion

    # Checking conditions for game termination by "mars" type
    total_checkers = sum(board_map.values())
    if total_checkers == 15:
        result["points"] = 2
        result["win_type"] = "mars"
        return result

    for i in range(6, 24):
        if board_map[i]:
            result["points"] = 2
            result["win_type"] = "mars"
            return result
    # endregion

    # Checking conditions for game termination by "oin" type
    result["points"] = 1
    result["win_type"] = "oin"
    return result
    # endregion

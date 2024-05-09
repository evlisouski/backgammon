def calculate(result_input):
    # home_board = range(0, 6)
    # outer_board = range(6, 12)
    # oponent_outer_board = range(12, 18)
    # oponent_home_board = range(18, 24)
    result = {"points": 0, "win_type": None}

    board_map = {int(i.number): int(i.checkers_count) for i in result_input.board.points}

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

    result["points"] = 1
    result["win_type"] = "oin"
    return result

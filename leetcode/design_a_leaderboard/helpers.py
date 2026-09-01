def run_leaderboard(solution_class: type, operations: list[str], inputs: list[list[int]]):
    board = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "Leaderboard":
            board = solution_class()
            results.append(None)
        elif op == "add_score" and board is not None:
            board.add_score(inputs[i][0], inputs[i][1])
            results.append(None)
        elif op == "top" and board is not None:
            results.append(board.top(inputs[i][0]))
        elif op == "reset" and board is not None:
            board.reset(inputs[i][0])
            results.append(None)
    return results, board


def assert_leaderboard(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True

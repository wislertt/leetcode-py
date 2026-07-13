def run_solve_sudoku(solution_class: type, board: list[list[str]]):
    import copy

    board_copy = copy.deepcopy(board)
    implementation = solution_class()
    implementation.solve_sudoku(board_copy)
    return board_copy


def assert_solve_sudoku(result: list[list[str]], board: list[list[str]]) -> bool:
    digits = set("123456789")
    for i in range(9):
        assert set(result[i]) == digits, f"Row {i} invalid"
        assert {result[r][i] for r in range(9)} == digits, f"Col {i} invalid"
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            box = {result[br + dr][bc + dc] for dr in range(3) for dc in range(3)}
            assert box == digits, f"Box {br},{bc} invalid"
    for r in range(9):
        for c in range(9):
            if board[r][c] != "." and board[r][c] != result[r][c]:
                raise AssertionError(f"Original cell {r},{c} changed")
    return True

def run_restore_matrix(solution_class: type, row_sum: list[int], col_sum: list[int]):
    implementation = solution_class()
    return implementation.restore_matrix(row_sum, col_sum)


def assert_restore_matrix(
    result: list[list[int]], row_sum: list[int], col_sum: list[int], expected: list[list[int]]
) -> bool:
    # Multiple valid matrices exist: validate the returned one instead of
    # comparing it with the sample output
    assert len(result) == len(row_sum)
    assert len(expected) == len(row_sum)
    for i, row in enumerate(result):
        assert len(row) == len(col_sum)
        assert all(value >= 0 for value in row)
        assert sum(row) == row_sum[i]
    for j, col_total in enumerate(col_sum):
        assert sum(row[j] for row in result) == col_total
    return True

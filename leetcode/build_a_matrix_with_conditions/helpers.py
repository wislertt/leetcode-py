def run_build_matrix(
    solution_class: type, k: int, row_conditions: list[list[int]], col_conditions: list[list[int]]
):
    implementation = solution_class()
    return implementation.build_matrix(k, row_conditions, col_conditions)


def assert_build_matrix(
    result: list[list[int]],
    k: int,
    row_conditions: list[list[int]],
    col_conditions: list[list[int]],
    valid: bool,
) -> bool:
    if not valid:
        assert result == []
        return True
    assert len(result) == k
    for row in result:
        assert len(row) == k
    positions = {}
    seen = set()
    for r in range(k):
        for c in range(k):
            value = result[r][c]
            if value != 0:
                assert 1 <= value <= k
                assert value not in seen
                seen.add(value)
                positions[value] = (r, c)
    assert len(seen) == k
    for above, below in row_conditions:
        assert positions[above][0] < positions[below][0]
    for left, right in col_conditions:
        assert positions[left][1] < positions[right][1]
    return True

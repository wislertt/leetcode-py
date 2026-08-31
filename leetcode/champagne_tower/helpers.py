def run_champagne_tower(solution_class: type, poured: int, query_row: int, query_glass: int):
    implementation = solution_class()
    return implementation.champagne_tower(poured, query_row, query_glass)


def assert_champagne_tower(result: float, expected: float) -> bool:
    # All flow amounts are dyadic rationals (repeated halving), so exact
    # equality holds in binary floating point
    assert result == expected
    return True

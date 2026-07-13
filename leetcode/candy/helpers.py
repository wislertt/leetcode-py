def run_candy(solution_class: type, ratings: list[int]):
    implementation = solution_class()
    return implementation.candy(ratings)


def assert_candy(result: int, expected: int) -> bool:
    assert result == expected
    return True

def run_maximize_sweetness(solution_class: type, sweetness: list[int], k: int):
    implementation = solution_class()
    return implementation.maximize_sweetness(sweetness, k)


def assert_maximize_sweetness(result: int, expected: int) -> bool:
    assert result == expected
    return True

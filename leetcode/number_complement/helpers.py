def run_find_complement(solution_class: type, num: int):
    implementation = solution_class()
    return implementation.find_complement(num)


def assert_find_complement(result: int, expected: int) -> bool:
    assert result == expected
    return True

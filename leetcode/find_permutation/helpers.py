def run_find_permutation(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.find_permutation(s)


def assert_find_permutation(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True

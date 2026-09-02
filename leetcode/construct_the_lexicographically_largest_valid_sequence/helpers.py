def run_construct_distanced_sequence(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.construct_distanced_sequence(n)


def assert_construct_distanced_sequence(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True

def run_h_index(solution_class: type, citations: list[int]):
    implementation = solution_class()
    return implementation.h_index(citations)


def assert_h_index(result: int, expected: int) -> bool:
    assert result == expected
    return True

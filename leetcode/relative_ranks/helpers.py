def run_find_relative_ranks(solution_class: type, score: list[int]):
    implementation = solution_class()
    return implementation.find_relative_ranks(score)


def assert_find_relative_ranks(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True

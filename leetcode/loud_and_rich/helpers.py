def run_loud_and_rich(solution_class: type, richer: list[list[int]], quiet: list[int]):
    implementation = solution_class()
    return implementation.loud_and_rich(richer, quiet)


def assert_loud_and_rich(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True

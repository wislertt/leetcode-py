def run_distinct_names(solution_class: type, ideas: list[str]):
    implementation = solution_class()
    return implementation.distinct_names(ideas)


def assert_distinct_names(result: int, expected: int) -> bool:
    assert result == expected
    return True

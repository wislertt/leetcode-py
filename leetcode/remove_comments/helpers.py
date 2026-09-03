def run_remove_comments(solution_class: type, source: list[str]):
    implementation = solution_class()
    return implementation.remove_comments(source)


def assert_remove_comments(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True

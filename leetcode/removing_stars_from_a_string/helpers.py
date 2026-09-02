def run_remove_stars(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.remove_stars(s)


def assert_remove_stars(result: str, expected: str) -> bool:
    assert result == expected
    return True

def run_simplify_path(solution_class: type, path: str):
    implementation = solution_class()
    return implementation.simplify_path(path)


def assert_simplify_path(result: str, expected: str) -> bool:
    assert result == expected
    return True

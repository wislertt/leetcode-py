def run_is_path_crossing(solution_class: type, path: str):
    implementation = solution_class()
    return implementation.is_path_crossing(path)


def assert_is_path_crossing(result: bool, expected: bool) -> bool:
    assert result == expected
    return True

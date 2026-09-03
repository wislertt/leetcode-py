def run_can_transform(solution_class: type, start: str, result: str):
    implementation = solution_class()
    return implementation.can_transform(start, result)


def assert_can_transform(result: bool, expected: bool) -> bool:
    assert result == expected
    return True

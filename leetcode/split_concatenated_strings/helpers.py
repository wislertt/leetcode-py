def run_split_looping_string(solution_class: type, strs: list[str]):
    implementation = solution_class()
    return implementation.split_looping_string(strs)


def assert_split_looping_string(result: str, expected: str) -> bool:
    assert result == expected
    return True

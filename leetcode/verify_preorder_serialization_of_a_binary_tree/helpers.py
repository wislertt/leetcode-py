def run_is_valid_serialization(solution_class: type, preorder: str):
    implementation = solution_class()
    return implementation.is_valid_serialization(preorder)


def assert_is_valid_serialization(result: bool, expected: bool) -> bool:
    assert result == expected
    return True

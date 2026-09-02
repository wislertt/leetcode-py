def run_convert_to_base_7(solution_class: type, num: int):
    implementation = solution_class()
    return implementation.convert_to_base_7(num)


def assert_convert_to_base_7(result: str, expected: str) -> bool:
    assert result == expected
    return True

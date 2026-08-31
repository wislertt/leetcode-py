def run_validate_stack_sequences(solution_class: type, pushed: list[int], popped: list[int]):
    implementation = solution_class()
    return implementation.validate_stack_sequences(pushed, popped)


def assert_validate_stack_sequences(result: bool, expected: bool) -> bool:
    assert result == expected
    return True

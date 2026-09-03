def run_is_one_bit_character(solution_class: type, bits: list[int]):
    implementation = solution_class()
    return implementation.is_one_bit_character(bits)


def assert_is_one_bit_character(result: bool, expected: bool) -> bool:
    assert result == expected
    return True

def run_number_of_beams(solution_class: type, bank: list[str]):
    implementation = solution_class()
    return implementation.number_of_beams(bank)


def assert_number_of_beams(result: int, expected: int) -> bool:
    assert result == expected
    return True

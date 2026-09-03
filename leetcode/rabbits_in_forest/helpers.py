def run_num_rabbits(solution_class: type, answers: list[int]):
    implementation = solution_class()
    return implementation.num_rabbits(answers)


def assert_num_rabbits(result: int, expected: int) -> bool:
    assert result == expected
    return True

def run_min_difficulty(solution_class: type, job_difficulty: list[int], d: int):
    implementation = solution_class()
    return implementation.min_difficulty(job_difficulty, d)


def assert_min_difficulty(result: int, expected: int) -> bool:
    assert result == expected
    return True

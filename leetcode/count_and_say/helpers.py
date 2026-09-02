def run_count_and_say(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.count_and_say(n)


def assert_count_and_say(result: str, expected: str) -> bool:
    assert result == expected
    return True

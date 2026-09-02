def run_poor_pigs(solution_class: type, buckets: int, minutes_to_die: int, minutes_to_test: int):
    implementation = solution_class()
    return implementation.poor_pigs(buckets, minutes_to_die, minutes_to_test)


def assert_poor_pigs(result: int, expected: int) -> bool:
    assert result == expected
    return True

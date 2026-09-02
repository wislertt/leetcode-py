def run_smallest_good_base(solution_class: type, n: str):
    implementation = solution_class()
    return implementation.smallest_good_base(n)


def assert_smallest_good_base(result: str, expected: str) -> bool:
    assert result == expected
    return True

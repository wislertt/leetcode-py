def run_kth_distinct(solution_class: type, arr: list[str], k: int):
    implementation = solution_class()
    return implementation.kth_distinct(arr, k)


def assert_kth_distinct(result: str, expected: str) -> bool:
    assert result == expected
    return True

def run_construct_array(solution_class: type, n: int, k: int):
    implementation = solution_class()
    return implementation.construct_array(n, k)


def assert_construct_array(result: list[int], k: int) -> bool:
    # Multiple valid arrangements exist; verify the result is a permutation
    # of 1..n whose adjacent differences have exactly k distinct values
    n = len(result)
    assert sorted(result) == list(range(1, n + 1))
    diffs = {abs(result[i] - result[i + 1]) for i in range(n - 1)}
    assert len(diffs) == k
    return True

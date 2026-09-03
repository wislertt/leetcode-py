def run_pancake_sort(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.pancake_sort(arr)


def assert_pancake_sort(result: list[int], arr: list[int], expected: list[int]) -> bool:
    # Multiple valid flip sequences exist; simulate the flips and
    # verify the array ends up sorted within the flip budget
    n = len(arr)
    assert len(result) <= 10 * n
    state = list(arr)
    for k in result:
        assert 1 <= k <= n
        for i in range(k // 2):
            state[i], state[k - 1 - i] = state[k - 1 - i], state[i]
    assert state == expected
    return True

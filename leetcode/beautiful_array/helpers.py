def run_beautiful_array(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.beautiful_array(n)


def assert_beautiful_array(result: list[int], expected: int) -> bool:
    # Any beautiful array is accepted; verify the result is a
    # permutation of [1, n] with no bad triple i < k < j
    assert len(result) == expected
    assert sorted(result) == list(range(1, expected + 1))
    pos = {v: i for i, v in enumerate(result)}
    for k in range(len(result)):
        for i in range(k):
            if pos.get(2 * result[k] - result[i], -1) > k:
                return False
    return True

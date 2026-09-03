def run_crack_safe(solution_class: type, n: int, k: int):
    implementation = solution_class()
    return implementation.crack_safe(n, k)


def assert_crack_safe(result: str, expected: tuple[int, int]) -> bool:
    # Any minimum-length de Bruijn sequence is accepted, so expected is the
    # (n, k) pair used to validate the result rather than one exact string
    n, k = expected
    assert len(result) == k**n + n - 1
    assert set(result) <= set("0123456789")
    assert len(set(result)) == k
    windows = [result[i : i + n] for i in range(k**n)]
    assert len(set(windows)) == k**n
    return True

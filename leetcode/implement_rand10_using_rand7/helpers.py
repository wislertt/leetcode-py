from .solution import Rand7


def run_rand10(solution_class: type, seed: int, n: int) -> tuple[list[int], int]:
    api = Rand7(seed)
    implementation = solution_class(api)
    results = [implementation.rand10() for _ in range(n)]
    return results, api.calls


def assert_rand10(result: tuple[list[int], int], expected: int) -> bool:
    values, calls = result
    assert len(values) == expected
    assert all(1 <= value <= 10 for value in values)
    # A correct uniform rand10() covers every value once the draw count is high
    if expected >= 100:
        assert len(set(values)) == 10
    # Rejection sampling averages ~2.45 rand7() calls per rand10() draw
    assert calls <= 6 * expected + 40
    return True

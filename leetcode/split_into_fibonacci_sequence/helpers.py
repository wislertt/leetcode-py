def run_split_into_fibonacci(solution_class: type, num: str):
    implementation = solution_class()
    return implementation.split_into_fibonacci(num)


def assert_split_into_fibonacci(result: list[int], expected: list[int]) -> bool:
    if not result and not expected:
        return True
    # Any valid split is accepted; validate structure instead of equality
    assert len(result) >= 3
    assert all(0 <= val < 2**31 for val in result)
    pieces = [str(val) for val in result]
    assert all(p == "0" or not p.startswith("0") for p in pieces)
    assert all(result[i] + result[i + 1] == result[i + 2] for i in range(len(result) - 2))
    assert "".join(pieces) == "".join(str(val) for val in expected)
    return True

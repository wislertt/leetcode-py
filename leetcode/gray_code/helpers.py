def run_gray_code(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.gray_code(n)


def assert_gray_code(result: list[int], expected_size: int) -> bool:
    # Multiple valid answers exist; verify the sequence is a valid
    # n-bit gray code rather than comparing against one fixed sequence
    n = expected_size.bit_length() - 1
    size = 1 << n
    assert len(result) == size
    assert result[0] == 0
    assert len(set(result)) == size
    assert all(0 <= value < size for value in result)
    diffs = [result[i] ^ result[i + 1] for i in range(size - 1)]
    assert all(bin(d).count("1") == 1 for d in diffs)
    assert bin(result[-1]).count("1") == 1
    return True

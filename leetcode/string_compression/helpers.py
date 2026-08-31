def run_compress(solution_class: type, chars: list[str]):
    implementation = solution_class()
    length = implementation.compress(chars)
    return length, chars[:length]


def assert_compress(result: tuple[int, list[str]], expected: list[str]) -> bool:
    length, compressed = result
    assert length == len(expected)
    assert compressed == expected
    return True

def expand_encoded(encoded: str) -> str:
    stack: list[tuple[str, int]] = []
    cur = ""
    num = ""
    for ch in encoded:
        if ch.isdigit():
            num += ch
        elif ch == "[":
            stack.append((cur, int(num)))
            cur = ""
            num = ""
        elif ch == "]":
            prev, k = stack.pop()
            cur = prev + cur * k
        else:
            cur += ch
    return cur


def run_encode(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.encode(s)


def assert_encode(result: str, source: str, expected_len: int) -> bool:
    assert expand_encoded(result) == source
    assert len(result) == expected_len
    return True

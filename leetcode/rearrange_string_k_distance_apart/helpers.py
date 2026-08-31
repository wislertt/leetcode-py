from collections import Counter


def run_rearrange_string(solution_class: type, s: str, k: int):
    implementation = solution_class()
    return implementation.rearrange_string(s, k)


def assert_rearrange_string(result: str, s: str, k: int) -> bool:
    # If no valid rearrangement exists, the only correct answer is the empty string.
    max_count = max(Counter(s).values())
    if k > 1 and max_count > (len(s) - 1) // k + 1:
        assert result == ""
    else:
        assert sorted(result) == sorted(s)
        last: dict[str, int] = {}
        for i, ch in enumerate(result):
            assert ch not in last or i - last[ch] >= k
            last[ch] = i
    return True

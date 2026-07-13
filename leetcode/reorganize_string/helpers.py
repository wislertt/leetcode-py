from collections import Counter


def run_reorganize_string(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.reorganize_string(s)


def assert_reorganize_string(result: str, s: str) -> bool:
    # If no valid rearrangement exists, the only correct answer is the empty string.
    max_count = max(Counter(s).values())
    if max_count > (len(s) + 1) // 2:
        assert result == ""
    else:
        assert sorted(result) == sorted(s)
        assert all(result[i] != result[i + 1] for i in range(len(result) - 1))
    return True

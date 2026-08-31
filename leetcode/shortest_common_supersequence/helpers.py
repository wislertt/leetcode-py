def run_shortest_common_supersequence(solution_class: type, str1: str, str2: str):
    implementation = solution_class()
    return implementation.shortest_common_supersequence(str1, str2)


def assert_shortest_common_supersequence(
    result: str, str1: str, str2: str, expected_length: int
) -> bool:
    def is_subsequence(sub: str, s: str) -> bool:
        it = iter(s)
        return all(c in it for c in sub)

    assert len(result) == expected_length
    assert is_subsequence(str1, result)
    assert is_subsequence(str2, result)
    return True

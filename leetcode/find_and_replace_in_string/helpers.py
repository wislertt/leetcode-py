def run_find_replace_string(
    solution_class: type, s: str, indices: list[int], sources: list[str], targets: list[str]
):
    implementation = solution_class()
    return implementation.find_replace_string(s, indices, sources, targets)


def assert_find_replace_string(result: str, expected: str) -> bool:
    assert result == expected
    return True

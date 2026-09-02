def run_most_visited_pattern(
    solution_class: type, username: list[str], timestamp: list[int], website: list[str]
):
    implementation = solution_class()
    return implementation.most_visited_pattern(username, timestamp, website)


def assert_most_visited_pattern(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True

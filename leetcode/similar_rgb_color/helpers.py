def run_similar_rgb(solution_class: type, color: str):
    implementation = solution_class()
    return implementation.similar_rgb(color)


def assert_similar_rgb(result: str, expected: str) -> bool:
    assert result == expected
    return True

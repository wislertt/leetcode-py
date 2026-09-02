def run_apply_substitutions(solution_class: type, replacements: list[list[str]], text: str):
    implementation = solution_class()
    return implementation.apply_substitutions(replacements, text)


def assert_apply_substitutions(result: str, expected: str) -> bool:
    assert result == expected
    return True

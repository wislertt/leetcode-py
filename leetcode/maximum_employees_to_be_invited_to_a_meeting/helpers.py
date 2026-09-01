def run_maximum_invitations(solution_class: type, favorite: list[int]):
    implementation = solution_class()
    return implementation.maximum_invitations(favorite)


def assert_maximum_invitations(result: int, expected: int) -> bool:
    assert result == expected
    return True

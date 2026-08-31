def run_num_unique_emails(solution_class: type, emails: list[str]):
    implementation = solution_class()
    return implementation.num_unique_emails(emails)


def assert_num_unique_emails(result: int, expected: int) -> bool:
    assert result == expected
    return True

from typing import List


def run_accounts_merge(solution_class: type, accounts: List[List[str]]):
    implementation = solution_class()
    return implementation.accounts_merge(accounts)


def assert_accounts_merge(result: List[List[str]], expected: List[List[str]]) -> bool:
    assert result == expected
    return True

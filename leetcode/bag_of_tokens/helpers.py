def run_bag_of_tokens_score(solution_class: type, tokens: list[int], power: int):
    implementation = solution_class()
    return implementation.bag_of_tokens_score(tokens, power)


def assert_bag_of_tokens_score(result: int, expected: int) -> bool:
    assert result == expected
    return True

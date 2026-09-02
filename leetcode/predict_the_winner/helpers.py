def run_predict_the_winner(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.predict_the_winner(nums)


def assert_predict_the_winner(result: bool, expected: bool) -> bool:
    assert result == expected
    return True

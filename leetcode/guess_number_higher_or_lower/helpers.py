from . import solution as solution_module


def run_guess_number(solution_class: type, n: int, pick: int):
    def make_guess(pick_value: int):
        def guess(num: int) -> int:
            if num > pick_value:
                return -1
            if num < pick_value:
                return 1
            return 0

        return guess

    solution_module.guess = make_guess(pick)
    implementation = solution_class()
    return implementation.guess_number(n)


def assert_guess_number(result: int, expected: int) -> bool:
    assert result == expected
    return True

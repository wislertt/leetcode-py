def run_food_ratings(solution_class: type, operations: list[str], inputs: list[list]):
    system = None
    results: list[str | None] = []
    for i, op in enumerate(operations):
        if op == "FoodRatings":
            system = solution_class(*inputs[i])
            results.append(None)
        elif op == "change_rating" and system is not None:
            system.change_rating(*inputs[i])
            results.append(None)
        elif op == "highest_rated" and system is not None:
            results.append(system.highest_rated(*inputs[i]))
    return results, system


def assert_food_ratings(result: list[str | None], expected: list[str | None]) -> bool:
    assert result == expected
    return True

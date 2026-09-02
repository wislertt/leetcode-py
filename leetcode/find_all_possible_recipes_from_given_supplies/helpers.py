def run_find_all_recipes(
    solution_class: type, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
):
    implementation = solution_class()
    return implementation.find_all_recipes(recipes, ingredients, supplies)


def assert_find_all_recipes(result: list[str], expected: list[str]) -> bool:
    assert sorted(result) == sorted(expected)
    return True

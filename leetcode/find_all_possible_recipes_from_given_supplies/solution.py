from collections import deque


class Solution:
    # Time: O(V + E) over recipes and ingredient references
    # Space: O(V + E)
    def find_all_recipes(
        self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
    ) -> list[str]:
        recipe_set = set(recipes)
        remaining = {r: len(ings) for r, ings in zip(recipes, ingredients, strict=True)}
        dependents: dict[str, list[str]] = {}
        for recipe, ings in zip(recipes, ingredients, strict=True):
            for ing in ings:
                dependents.setdefault(ing, []).append(recipe)
        made: list[str] = []
        queue: deque[str] = deque(supplies)
        queue.extend(recipe for recipe in recipes if remaining[recipe] == 0)
        while queue:
            item = queue.popleft()
            if item in recipe_set:
                made.append(item)
            for recipe in dependents.get(item, ()):
                remaining[recipe] -= 1
                if remaining[recipe] == 0:
                    queue.append(recipe)
        return made

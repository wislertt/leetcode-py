import heapq


class FoodRatings:
    # Time: init O(n), change_rating O(log n), highest_rated amortized O(log n)
    # Space: O(n) for the rating/cuisine maps and one lazy heap per cuisine
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]) -> None:
        self.rating: dict[str, int] = dict(zip(foods, ratings, strict=True))
        self.cuisine = dict(zip(foods, cuisines, strict=True))
        self.heaps: dict[str, list[tuple[int, str]]] = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings, strict=True):
            self.heaps.setdefault(cuisine, []).append((-rating, food))
        for heap in self.heaps.values():
            heapq.heapify(heap)

    # Time: O(log n)
    # Space: O(1) amortized (each pushed entry is popped at most once)
    def change_rating(self, food: str, new_rating: int) -> None:
        self.rating[food] = new_rating
        # The old entry for this food is left behind as stale; highest_rated
        # discards entries whose rating no longer matches the current one.
        heapq.heappush(self.heaps[self.cuisine[food]], (-new_rating, food))

    # Time: O(log n) amortized
    # Space: O(1)
    def highest_rated(self, cuisine: str) -> str:
        heap = self.heaps[cuisine]
        while True:
            neg_rating, food = heap[0]
            if -neg_rating == self.rating[food]:
                return food
            heapq.heappop(heap)

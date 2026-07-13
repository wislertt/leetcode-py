class Solution:
    # Time: O(n log n)
    # Space: O(n) for sorting
    def num_rescue_boats(self, people: list[int], limit: int) -> int:
        people.sort()
        boats = 0
        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats

class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def sort_people(self, names: list[str], heights: list[int]) -> list[str]:
        order = sorted(range(len(heights)), key=heights.__getitem__, reverse=True)
        return [names[i] for i in order]

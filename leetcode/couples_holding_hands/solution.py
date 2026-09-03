class Solution:
    # Time: O(n)
    # Space: O(n)
    def min_swaps_couples(self, row: list[int]) -> int:
        arr = list(row)
        pos = {person: i for i, person in enumerate(arr)}
        swaps = 0
        for i in range(0, len(arr), 2):
            partner = arr[i] ^ 1
            if arr[i + 1] != partner:
                j = pos[partner]
                other = arr[i + 1]
                arr[i + 1], arr[j] = partner, other
                pos[partner] = i + 1
                pos[other] = j
                swaps += 1
        return swaps

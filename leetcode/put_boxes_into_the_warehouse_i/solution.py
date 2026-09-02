class Solution:
    # Time: O(m + n log n), Space: O(n) for effective heights
    def max_boxes_in_warehouse(self, boxes: list[int], warehouse: list[int]) -> int:
        # A box of height b can occupy room i iff b <= min(warehouse[0..i]):
        # it must survive every room on the way and fit in room i itself.
        lowest: list[int] = []
        reachable = warehouse[0]
        for height in warehouse:
            reachable = min(reachable, height)
            lowest.append(reachable)

        # Smallest box pairs with the smallest usable (rightmost) room.
        placed = 0
        room = len(lowest) - 1
        for box in sorted(boxes):
            while room >= 0 and lowest[room] < box:
                room -= 1
            if room < 0:
                break
            placed += 1
            room -= 1
        return placed

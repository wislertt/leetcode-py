class Solution:
    # Time: O(n^2) (n <= 2000, insertion into a list is linear)
    # Space: O(n)
    def reconstruct_queue(self, people: list[list[int]]) -> list[list[int]]:
        # Tall first (so later, shorter insertions cannot invalidate earlier
        # placements), then fewest taller-in-front first; insert at index k.
        ordered = sorted(people, key=lambda p: (-p[0], p[1]))
        queue: list[list[int]] = []
        for height, k in ordered:
            queue.insert(k, [height, k])
        return queue

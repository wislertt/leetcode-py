from collections import deque


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def deck_revealed_increasing(self, deck: list[int]) -> list[int]:
        queue: deque[int] = deque(range(len(deck)))
        result: list[int] = [0] * len(deck)
        for card in sorted(deck):
            # Reveal the card at the front position
            result[queue.popleft()] = card
            # Move the next position to the bottom
            if queue:
                queue.append(queue.popleft())
        return result

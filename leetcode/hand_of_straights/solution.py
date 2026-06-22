from collections import Counter


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def is_n_straight_hand(self, hand: list[int], group_size: int) -> bool:
        if len(hand) % group_size != 0:
            return False

        count: Counter[int] = Counter(hand)
        for card in sorted(count):
            if count[card] == 0:
                continue
            frequency = count[card]
            # Greedily form `frequency` groups starting at `card`
            for offset in range(group_size):
                next_card = card + offset
                if count[next_card] < frequency:
                    return False
                count[next_card] -= frequency
        return True

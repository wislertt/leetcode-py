class Solution:
    # Time: O(n log n)
    # Space: O(n) for the sorted copy
    def bag_of_tokens_score(self, tokens: list[int], power: int) -> int:
        tokens = sorted(tokens)
        left, right = 0, len(tokens) - 1
        score = 0
        best = 0
        while left <= right:
            if power >= tokens[left]:
                # Cheapest token face-up for score
                power -= tokens[left]
                left += 1
                score += 1
                best = max(best, score)
            elif score >= 1:
                # Most expensive token face-down for power
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                break
        return best

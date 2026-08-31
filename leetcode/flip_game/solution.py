class Solution:
    # Time: O(n^2) where n is the string length
    # Space: O(n) excluding the output
    def generate_possible_next_moves(self, current_state: str) -> list[str]:
        results: list[str] = []
        for i in range(len(current_state) - 1):
            if current_state[i : i + 2] == "++":
                results.append(current_state[:i] + "--" + current_state[i + 2 :])
        return results

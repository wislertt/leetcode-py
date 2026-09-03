class Solution:
    # Time: O(n + m)
    # Space: O(m)
    def find_restaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        index_in_list2 = {s: i for i, s in enumerate(list2)}
        best_sum = len(list1) + len(list2)
        result: list[str] = []
        for i, s in enumerate(list1):
            j = index_in_list2.get(s)
            if j is None:
                continue
            total = i + j
            if total < best_sum:
                best_sum = total
                result = [s]
            elif total == best_sum:
                result.append(s)
        return result

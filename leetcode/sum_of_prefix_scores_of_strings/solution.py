class Solution:
    # Time: O(total characters across all words)
    # Space: O(total characters) for the trie
    def sum_prefix_scores(self, words: list[str]) -> list[int]:
        children: list[dict[str, int]] = [{}]
        counts: list[int] = [0]

        for word in words:
            node = 0
            for ch in word:
                nxt = children[node].get(ch)
                if nxt is None:
                    nxt = len(children)
                    children[node][ch] = nxt
                    children.append({})
                    counts.append(0)
                node = nxt
                counts[node] += 1

        answer: list[int] = []
        for word in words:
            node = 0
            total = 0
            for ch in word:
                node = children[node][ch]
                total += counts[node]
            answer.append(total)
        return answer

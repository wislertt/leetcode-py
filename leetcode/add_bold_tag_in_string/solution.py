class Solution:
    # Time: O(|s| * sum|words| * |s|) with find; effectively O(n * m)
    # Space: O(n)
    def add_bold_tag(self, s: str, words: list[str]) -> str:
        mask = [False] * len(s)
        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start, start + len(word)):
                    mask[i] = True
                start = s.find(word, start + 1)
        out: list[str] = []
        for i, ch in enumerate(s):
            if mask[i] and (i == 0 or not mask[i - 1]):
                out.append("<b>")
            out.append(ch)
            if mask[i] and (i == len(s) - 1 or not mask[i + 1]):
                out.append("</b>")
        return "".join(out)

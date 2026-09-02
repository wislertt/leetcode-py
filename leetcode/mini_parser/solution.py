from __future__ import annotations


class NestedInteger:
    def __init__(self, value: int | None = None) -> None:
        self._integer: int | None = value
        self._list: list[NestedInteger] | None = None if value is not None else []

    def is_integer(self) -> bool:
        return self._list is None

    def add(self, elem: NestedInteger) -> None:
        items = self._list
        if items is None:
            items = []
            self._integer = None
            self._list = items
        items.append(elem)

    def set_integer(self, value: int) -> None:
        self._integer = value
        self._list = None

    def get_integer(self) -> int | None:
        return self._integer

    def get_list(self) -> list[NestedInteger] | None:
        return self._list


class Solution:
    # Time: O(n) - each character is consumed exactly once
    # Space: O(d) - stack holds one NestedInteger per open bracket (d = nesting depth)
    def deserialize(self, s: str) -> NestedInteger:
        stack: list[NestedInteger] = []
        result: NestedInteger | None = None
        num: int | None = None
        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit() or char == "-":
                end = i + 1
                while end < len(s) and s[end].isdigit():
                    end += 1
                num = int(s[i:end])
                i = end
                continue
            if char == "[":
                stack.append(NestedInteger())
            else:
                if num is not None:
                    stack[-1].add(NestedInteger(num))
                    num = None
                if char == "]":
                    top = stack.pop()
                    if stack:
                        stack[-1].add(top)
                    else:
                        result = top
            i += 1
        return result if result is not None else NestedInteger(num)

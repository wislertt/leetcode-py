class LockingTree:
    # Time: __init__ O(n), lock O(1), unlock O(1), upgrade O(n) per call
    # Space: O(n)
    def __init__(self, parent: list[int]) -> None:
        self.parent = parent
        self.children: list[list[int]] = [[] for _ in parent]
        for node, par in enumerate(parent):
            if par != -1:
                self.children[par].append(node)
        self.locked_by: dict[int, int] = {}

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked_by:
            return False
        self.locked_by[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked_by.get(num) != user:
            return False
        del self.locked_by[num]
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked_by or self._locked_ancestor(num) or not self._locked_descendant(num):
            return False
        self._release_descendants(num)
        self.locked_by[num] = user
        return True

    def _locked_ancestor(self, num: int) -> bool:
        node = self.parent[num]
        while node != -1:
            if node in self.locked_by:
                return True
            node = self.parent[node]
        return False

    def _locked_descendant(self, num: int) -> bool:
        stack = [num]
        while stack:
            node = stack.pop()
            for child in self.children[node]:
                if child in self.locked_by:
                    return True
                stack.append(child)
        return False

    def _release_descendants(self, num: int) -> None:
        stack = [num]
        while stack:
            node = stack.pop()
            for child in self.children[node]:
                self.locked_by.pop(child, None)
                stack.append(child)

class Solution:
    # Time: O(m log m) for sorting meetings plus near-linear union-find passes
    # Space: O(n) for the parent array
    def find_all_people(self, n: int, meetings: list[list[int]], first_person: int) -> list[int]:
        parent = list(range(n))

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(a: int, b: int) -> None:
            root_a, root_b = find(a), find(b)
            if root_a != root_b:
                parent[root_a] = root_b

        known = {0, first_person}
        sorted_meetings = sorted(meetings, key=lambda meeting: meeting[2])
        i = 0
        total = len(sorted_meetings)
        while i < total:
            time = sorted_meetings[i][2]
            participants: set[int] = set()
            while i < total and sorted_meetings[i][2] == time:
                x, y, _ = sorted_meetings[i]
                union(x, y)
                participants.update((x, y))
                i += 1
            knower_roots = {find(p) for p in participants if p in known}
            for person in participants:
                if find(person) in knower_roots:
                    known.add(person)
            for person in participants:
                parent[person] = person
        return list(known)

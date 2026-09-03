from bisect import bisect_right


class TopVotedCandidate:
    # Time: O(n) to build the leader timeline
    # Space: O(n) for the leader timeline
    def __init__(self, persons: list[int], times: list[int]) -> None:
        self.times = times
        self.leaders: list[int] = []
        counts: dict[int, int] = {}
        leader = -1
        for person in persons:
            counts[person] = counts.get(person, 0) + 1
            if counts[person] >= counts.get(leader, 0):
                leader = person
            self.leaders.append(leader)

    # Time: O(log n)
    # Space: O(1)
    def q(self, t: int) -> int:
        return self.leaders[bisect_right(self.times, t) - 1]

class Solution:
    # Time: O(n)
    # Space: O(1)
    def circular_array_loop(self, nums: list[int]) -> bool:
        n = len(nums)

        def nxt(i: int) -> int:
            return (i + nums[i]) % n

        for start in range(n):
            if nums[start] == 0:
                continue
            forward = nums[start] > 0

            def ok(j: int, forward: bool = forward) -> bool:
                return nums[j] != 0 and (nums[j] > 0) == forward

            slow = start
            fast = nxt(slow)
            while ok(fast) and ok(nxt(fast)):
                if slow == fast:
                    if nxt(slow) != slow:
                        return True
                    break
                slow = nxt(slow)
                fast = nxt(nxt(fast))

            # The walk from `start` cannot yield a valid cycle; mark it dead.
            i = start
            for _ in range(n):
                if not ok(i):
                    break
                nums[i], i = 0, nxt(i)
        return False

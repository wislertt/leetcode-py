class Solution:
    # Time: O(n)
    # Space: O(1) excluding the output array
    def get_maximum_xor(self, nums: list[int], maximum_bit: int) -> list[int]:
        mask = (1 << maximum_bit) - 1
        total = 0
        for num in nums:
            total ^= num

        answer: list[int] = []
        for num in reversed(nums):
            answer.append(total ^ mask)
            total ^= num
        return answer

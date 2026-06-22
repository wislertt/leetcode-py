class Solution:
    # Time: O(n) average, O(n^2) worst
    # Space: O(1)
    def find_kth_largest(self, nums: list[int], k: int) -> int:
        target_index = len(nums) - k

        def quickselect(left: int, right: int) -> int:
            pivot = nums[right]
            store = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[store], nums[i] = nums[i], nums[store]
                    store += 1
            nums[store], nums[right] = nums[right], nums[store]

            if store == target_index:
                return nums[store]
            if store < target_index:
                return quickselect(store + 1, right)
            return quickselect(left, store - 1)

        return quickselect(0, len(nums) - 1)

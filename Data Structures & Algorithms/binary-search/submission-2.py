class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        # cut search space in half repeatedly
        # check middle element == target -> return index
        # if target > middle elem -> search right half
        # if target < middle elem -> search left half
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
        
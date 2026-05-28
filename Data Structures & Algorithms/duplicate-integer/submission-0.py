class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            if num in nums[i+1:]:
                return True
        return False

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        k = 0 
        count = 0

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff == 1:
                count += 1
                if count > k:
                    k = count
            elif diff == 0:
                continue
            else:
                count = 0
        

        return k + 1 if nums != [] else 0
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # initial thoughts
        # triple for loop to find all possible combinations
        # three numbers that add up to zero
        # no duplicate arrays
        # sort input array
        # duplicate values will be next to each other
        # skip duplicates
        # to sum up to zero we need negative numbers and positive numbers
        # so if we are past negative numbers there are no more 
        # possible combinations
        # we will loop forward skipping duplicate
        # left and right pointer to find the other two numbers
        # if sum > 0 we will shrink right pointer (right-1)
        # if sum < 0 we will shrink left pointer (left+1)
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            # skip duplicates
            if i > 0 and num == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return result
        
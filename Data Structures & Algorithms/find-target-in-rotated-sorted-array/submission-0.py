class Solution:
    def search(self, nums: List[int], target: int) -> int:
       # brute force
       # check every value
       # O(n)
       #
       # similar to find min in rotated array
       # binary search requirs a sorted array
       # there are two portions of the array that are sorted
       # if middle value is part of left sorted
       # and target is less than left pointer
       # search right (l = m + 1) 
       # else
       # search left
       # if in the sorted part of the array than 
       # just perform traditional binary search

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            
            # left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # right sorted portion
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1


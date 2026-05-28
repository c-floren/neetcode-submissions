class Solution:
    def findMin(self, nums: List[int]) -> int:
        # intuition:
        # traditional binary search requires a sorted array
        # rotated array comes from a sorted array
        # two sorted parts of the array
        # sort again method --> O(n log n)
        # 
        # brute force: pass through the array to find min
        # optimal: binary search hint originally sorted
        # set middle as minimum
        # find if the middle value is grouped with the
        # left sorted portion
        # search right sorted portion
        # nums[m] >= nums[l]
        #   search right
        # else
        #   search left
        # only works for rotated array
        # if new group regularly sorted
        # just check leftmost value
        # is less than current minimum value

        result = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            
            m = (l + r) // 2
            result = min(result, nums[m])
            # middle a part of left sorted portion
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return result





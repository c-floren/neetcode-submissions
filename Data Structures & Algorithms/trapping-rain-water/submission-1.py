class Solution:
    def trap(self, height: List[int]) -> int:
        # initial thoughts:
        # area can trap water if there exists a bar equal or greater
        # height after current bar
        # if the height goes down but doesn't go back up
        # then water cannot be contained
        # endpoints can't contain water
        # I need to keep track of the current bar
        # move forward until another equal or taller bar found
        # calculate the area using shorter bar height and length
        # if i move forward and it is still greater calculate area
        #
        # Question: how do I calculate irregular shape area?
        # I could calculate the area from the taller bars and length
        # and subtract the shorter bars from it
        #
        # Two Pointer
        # Time: O(n)
        # Space: O(1)
        # left pointer at start of height
        # right pointer at end of height
        # we're keeping track of max left and right height
        # if max left pointer less than or equal to max right pointer
        # shift left and calculate area: maxL - height[L]
        # update l_max
        # add area to result
        # 
        # else
        # shift right pointer and calculate area: maxR - height[R]
        # add area to result
        # if height is empty return 0       

        if not height: return 0


        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        result = 0


        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                result += leftMax - height[l] 
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                result += rightMax - height[r]
        
        return result

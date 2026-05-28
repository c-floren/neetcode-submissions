class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # initial thoughts:
        # can't sort bc index matters
        # brute force, check every container possible
        # double for loop and calculate max area
        # container only as tall as shorter height
        # area = shorter height * length (height2 index - height1 index)
        # max_area updated with area if area > max_area
        # shrink from shorter height side
        # repeat the process

        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
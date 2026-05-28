class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # intuition:
        # area increases as L or/and H increases
        # longest L = length of heights
        # highest H = greatest height 
        # H is limited by shortest height within L
        # 
        # understanding the example
        # ex. heights = [7,1,7,2,2,4]
        # longest L = 6 H = 1 -> A = 6 (not greatest area)
        # widest H = 7 (two) 
        # H = 1 L = 3 -> A = 3 or 
        # H = 2 L = 4 -> A = 8 (greatest)
        #
        # 
        # Brute force: O(n^2)
        # double for loop scans all possible rectangles
        # 
        # stack
        # monotonic increasing
        # will hold index and height
        # append to stack
        # if curr height < top of stack
        # calculate the area
        # update max area (max(max_area, area))
        # and then pop top of stack
        # append curr index and height
        # time O(n)

        stack = [] # pair: [index, height]
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
        
        # because increasing heights L can be extended to end of stack
        # from the current position
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initial thoughts:
        # order matters because i represents days (no sorting)
        # brute force
        # double forloop O(n^2) 
        # worst case traverse the whole list - i for each iteration
        #
        # stack idea (time: O(n), space: O(n))
        # stack pairs [temperature, index]
        # we have to remember index of previous temperatures before
        # greater temp
        # monotonic decreasing order stack: decreasing order to top
        # if temp > top of stack calculate difference between indices
        # that will tell us how many days it took
        # then pop from stack and append next temp
        # if not greater than any val in stack append to stack
        # result default value 0

        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            # while curr temp is greater than top temp
            # update result at corresponding index with number of days
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                # curr temp index - stack index = number of days
                result[stackInd] = i - stackInd
            stack.append([t, i])
        return result
        
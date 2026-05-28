class Solution:
    def isValid(self, s: str) -> bool:
        # start with opening parentheses
        # we need matching closing parentheses
        # if we have matches we can move on to check next pair
        # 
        parentheses = {")":"(", "]":"[", "}":"{"}
        stack = []
        for char in s:
            # if char is closing par
            if char in parentheses:
                # if open par matching closing par move on to next pair
                if stack and stack[-1] == parentheses[char]:
                    stack.pop()
                else:
                    return False
            # add open par to stack
            else:
                stack.append(char)
        
        # if stack is empty, valid parentheses is true
        return not stack
        
        # time complexity: O(n)
        # space complexity: O(n) (stack size of s)

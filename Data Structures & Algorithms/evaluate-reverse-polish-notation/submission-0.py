class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initial thoughts:
        # The numbers and operations need to be
        # completed left to right
        # ex. tokens = ["1","2","+","3","*","4","-"]
        # 1 + 2 = 3 then 3 * 3 = 9 then 9 - 4
        # using stack
        # add to stack while number
        # once an operation is found
        # pop twice from the stack
        # to make sure subtraction/division works well
        # the second pop must go before the operator
        # and first pop after the operator
        # these are strings so we will have to convert to numbers
        # to perform operations

        # initialize stack
        stack = []

        # loop forward through tokens
        for i, t in enumerate(tokens):
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "-":
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif t == "/":
                x, y = stack.pop(), stack.pop()
                stack.append(int(y / x))
            else:
                stack.append(int(t))
        return stack[-1]

        # time complexity is O(n)
        # space complexity is O(n)


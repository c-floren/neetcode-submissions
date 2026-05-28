class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # initial thoughts:
        # move as fleet when car catches up to speed and position
        # cannot pass therefore car that caught up slows down to 
        # speed of car in front
        #
        # visualizing it: loop until all cars reach destination
        # each iteration add speed to current position update position
        # when reach car ahead position joined the car fleet
        # originally there are n numbers of car fleets
        # because positions are all unique at the start
        # number decreases as the cars catch up
        #
        # time O(nlogn) space O(n)
        # sort speed and position by position
        # stack top will be the furthest ahead
        stack = []
        # array of pairs
        pair = [[p, s] for p, s in zip(position, speed)]

        for p, s in sorted(pair, reverse=True):
           stack.append((target - p) / s)
           if len(stack) >= 2 and stack[-1] <= stack[-2]:
              stack.pop()
        return len(stack)


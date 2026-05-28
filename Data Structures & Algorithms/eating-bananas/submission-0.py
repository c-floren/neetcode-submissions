class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # intuition:
        # len(p) <= h
        # min k = 1
        # max k = max(piles)
        # brute force:
        # try every k = [1,...,max(piles)]
        # first k that allows all the piles to be eaten
        # is the min k
        # time(max(piles) * len(piles))
        # binary search: time (O(log(max(piles))) * len(piles))
        # middle will be k we'll try
        # if middle valid, save as potential solution
        # try bs on smaller values to see if there is a smaller valid k
        # otherwise try bs on larger values
        # update k with min(prev, curr)

        l, r = 1, max(piles)
        res = r # max value k can be

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / k)
            
            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res





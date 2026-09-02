class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (r + l) // 2
            sum = 0
            for p in piles:
                sum += math.ceil(p/mid)
            
            if sum <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res
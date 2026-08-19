class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = collections.deque()
        l = r = 0
        output = []

        while r < len(nums):
            while maxes and nums[maxes[-1]] < nums[r]:
                maxes.pop()
            maxes.append(r)

            if l > maxes[0]:
                maxes.popleft()

            if r + 1 >= k:
                output.append(nums[maxes[0]])
                l += 1
            
            r += 1
        
        return output
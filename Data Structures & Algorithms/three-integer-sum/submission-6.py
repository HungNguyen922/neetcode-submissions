class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        numLen = len(nums)
        for i in range(numLen):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l = i+1
            r = numLen-1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return output

                
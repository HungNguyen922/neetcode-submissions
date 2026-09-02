class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[0]

        while l <= r:
            # we have 2 cases, we are either
                # in the completed sorted section
                    # in this case we can just return the left
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
                # not in the completely sorted section
                    # in this case we want to compare m val to l val

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
            

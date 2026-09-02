class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2
            # if nums[m] is less than both edges,
                # check its left neighbor: if it's greater than that shift r to mid - 1
                    #if it's lesser then return the value
            #if nums[m] is greater than both edges,
                #l = m + 1
            # else, then the viewed segment has to be sorted
                #return the min of nums[l] and nums[r]

            if nums[m] <= nums[l] and nums[m] < nums[r]:
                if nums[m] < nums[m-1]:
                    return nums[m]
                else:
                    r = m - 1
            elif nums[m] > nums[l] and nums[m] > nums[r]:
                l = m + 1
            else:
                return min(nums[l], nums[r])
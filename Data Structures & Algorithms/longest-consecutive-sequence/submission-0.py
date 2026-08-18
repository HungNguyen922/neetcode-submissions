class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert list to set
        # iterate through the set
        # if num -1 exists; continue
        # if num -1 does not, look for num +1 until you can't

        mySet = set(nums)
        longest = 0

        for num in mySet:
            if num - 1 in mySet:
                continue
            else:
                temp = 1
                while num + temp in mySet:
                    temp += 1
                longest = max(longest, temp)
        
        return longest

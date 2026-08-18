class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        prefix, postfix = [1] * numsLength, [1] * numsLength

        product = 1
        for i in range(numsLength):
            product *= nums[i]
            prefix[i] = product
        
        product = 1
        for i in range(numsLength-1, -1, -1):
            product *= nums[i]
            postfix[i] *= product

        output = [0] * numsLength

        for i in range(numsLength):
            if i == 0:
                output[i] = postfix[i+1]
            elif i == numsLength-1:
                output[i] = prefix[i-1]
            else:
                output[i] = prefix[i-1] * postfix[i+1]

        return output
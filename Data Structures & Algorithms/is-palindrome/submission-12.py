class Solution:
    def isPalindrome(self, s: str) -> bool:
        # odd and even length string cases
        # 2 pointer approach
        # even case set l = 0 and r = l + 1
            # while l and r are still in bounds of the string, expand outwards
        # odd case set l, r, = 0
            # while l and are are still in bounds of the string, expand outwards

        # since both approaches are very similar we can build a helper function that just takes in the parameters
        # then we just run the function twice, once with each parameter option
        
        clean = "".join(char for char in s if char.isalnum()).lower()
        print(clean)
        strLen = len(clean)
        if strLen % 2 == 0:
            return self.palindromeHelper(strLen//2 - 1, strLen//2, clean)
        else:
            return self.palindromeHelper(strLen//2, strLen//2, clean)

    def palindromeHelper(self, l: int, r: int, s: str) -> bool:
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                return False
        return True
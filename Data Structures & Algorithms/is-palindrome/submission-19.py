class Solution:
    def isPalindrome(self, s: str) -> bool:
        # checking just 1 palindrome
        string = "".join(char for char in s if char.isalnum()).lower()

        l = 0
        r = len(string) - 1

        while l <= r:
            if string[l] == string[r]:
                l += 1
                r -= 1
            else:
                return False

        return True
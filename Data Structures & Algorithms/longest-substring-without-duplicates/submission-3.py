class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = deque()
        longest = 0

        for char in s:
            if char not in string:
                string.append(char)
            else:
                longest = max(longest, len(string))
                while string[0] != char:
                    string.popleft()
                string.popleft()
                string.append(char)

        print(string)
        longest = max(longest, len(string))
        return longest
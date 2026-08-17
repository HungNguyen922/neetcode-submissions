class Solution:

    def encode(self, strs: List[str]) -> str:
        # returns  a string
        output = ""
        for word in strs:
            output += str(len(word)) + '#' + word
        return output

    def decode(self, s: str) -> List[str]:
        # returns a list
        output, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            output.append(s[j+1:j+length+1])
            i = j + length + 1
        
        return output

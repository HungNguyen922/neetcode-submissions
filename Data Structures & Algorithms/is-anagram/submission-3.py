class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}

        if len(s) != len(t):
            return False
            
        for letter in s:
            if letter in sDict:
                sDict[letter] += 1
            else:
                sDict[letter] = 1
        
        for letter in t:
            if letter in tDict:
                tDict[letter] += 1
            else:
                tDict[letter] = 1

        for letter in sDict:
            if letter in s and letter in t:
                if sDict[letter] != tDict[letter]:
                    return False
            else:
                return False

        return True
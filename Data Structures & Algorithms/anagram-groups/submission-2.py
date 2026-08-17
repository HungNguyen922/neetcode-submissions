class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # have a dict to divide each anagram grouping
        fullDict = {}

        # have a key for the fullDict based on char freq in each word
        for word in strs:
            counts = [0] * 26
            for ch in word:
                counts[ord(ch) - ord('a')] += 1
            key = tuple(counts)

            if key not in fullDict:
                fullDict[key] = []
            fullDict[key].append(word)
        
        output = []
        for key in fullDict:
            output.append(fullDict[key])
        return output

        
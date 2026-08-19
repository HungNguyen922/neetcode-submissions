class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # i need a has of s1 to keep track of the char frequencies
        s1Freqs = dict(Counter(s1))
        # the s2Freqs is going to be updated overtime as i update the sliding window
        # this allows me to compare each window to the character frequencies  in s1
        s2Freqs = dict()

        # i want the sliding window focused on s2
        # that way i can check if i hit a character in s1.
        # then i begin updating s2Freqs and check for validity

        l = 0
        for r in range(len(s2)):
            if s2[r] not in s1:
                l += 1
                if s2Freqs:
                    s2Freqs = dict()
                continue
            else:
                s2Freqs[s2[r]] = 1 + s2Freqs.get(s2[r], 0)
                if s2Freqs.items() == s1Freqs.items():
                    return True
                while s2Freqs[s2[r]] > s1Freqs[s2[r]]:
                    s2Freqs[s2[l]] -= 1
                    l += 1
        return False
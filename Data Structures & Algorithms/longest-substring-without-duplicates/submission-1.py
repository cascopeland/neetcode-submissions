class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letterSet = set()
        l = 0
        maxLength = 0
        for r in range(len(s)):
            while s[r] in letterSet:
                letterSet.remove(s[l])
                l += 1
            letterSet.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        return maxLength

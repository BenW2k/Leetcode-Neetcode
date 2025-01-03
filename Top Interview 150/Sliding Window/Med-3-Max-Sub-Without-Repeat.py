class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0 # initialise left side
        charSet = set() # set because they don't store duplicates
        res = 0 #len of max substring

        for r in range(len(s)): # using r as the index, length
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, (r - l + 1))
        return res
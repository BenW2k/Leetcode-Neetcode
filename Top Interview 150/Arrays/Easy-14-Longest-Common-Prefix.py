class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans="" # initialise empty string
        strs = sorted(strs) # sorts the string lexicographically
        first = strs[0] # This is the string in the list
        last = strs[-1] # This is the last string in the list
        for i in range(min(len(first), len(last))): # this finds the minimum string length between the first and last words in the list
            if first[i] != last[i]: # if the characters aren't the same return the ans, which is the longest common prefix
                return ans
            ans += first[i]
        return ans


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        res = []
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return "".join(res)
            res.append(strs[0][i])
        return "".join(res)
                
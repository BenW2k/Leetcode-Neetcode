class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        map = {}

        seen_list = []

        for i in range(len(s)):
            if s[i] not in map:
                if t[i] in seen_list:
                    return False
                map[s[i]] = t[i]
                seen_list.append(t[i])
            else:
                if map[s[i]] != t[i]:
                    return False
        return True
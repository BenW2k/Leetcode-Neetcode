class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # This problem is about seeing if the strings in one string can be used as a direct 1:1 mapping to another string
        # each letters can only pair with one letter
        # Used a hashmap to store pairs and a separate array to store letters from the second string to ensure that we don't have repeats.
        # I think this solution is O(n) because the maximum amount of times (assuming we're only dealing with english letters) that we could possibly reach the nested
        # iteration through the seen list is 26 (the 26 letters in the alphabet) hence not making it O(n^2)
        
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
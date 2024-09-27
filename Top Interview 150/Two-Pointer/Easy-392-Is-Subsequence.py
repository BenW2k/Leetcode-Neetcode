class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j = 0 # sets substring pointer to 0
        if len(s) <= 0: #gets rid of edge case for substring being empty (says to return True if so)
            return True
        else:
            for i in range(len(t)): # Loops through t
                if s[j] == t[i]:
                    if j == len(s) - 1 : # returns true as this shows all chars in s are in t
                        return True
                    j += 1 # increment j to check for next character
            return False # If it doesn't escape loop earlier, then it's False
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j = 0 # initial pointer  for the substring
        if len(s) <= 0: # edge case for if substring is empty
            return True
        else:
            for i in range(len(t)):
                if s[j] == t[i]: # if letters are equal
                    if j == len(s) - 1 :  # if equal then substring pointer is at the end meaning it is in the parent string
                        return True
                    j += 1
            return False # Else return false


        
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0 # Creates the Two Pointers
        while i < len(s) and j < len(t): # Checks if the true conditions have been met and it is still in range of the list
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
    
# Notes - 
# uses i to as a way to check to if s is in t by counting every time a character in s is found in t and comparing the value of i to the length of t (same value means s is in t)
# uses check at the end to send the boolean back.
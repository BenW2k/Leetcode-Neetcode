class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        word = ''.join(ch for ch in s if ch.isalnum()).lower() # creates a string from only valid alphanumeric characters and converts them to lowercase
        i = 0 # pointer for left side of array
        j = len(word) - 1 # pointer for right side of array (remember -1 because it will be used as an index)

        while i <= j:
            if word[i] != word[j]:
                return False
            i +=1
            j -=1
        return True
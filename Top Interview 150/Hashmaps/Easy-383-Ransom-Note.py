class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag = {}
        # Firstly adding all letters in the magazine string to mag hashmap
        # Also adds the frequency that each letter occurs
        for i in range(len(magazine)):
            if magazine[i] not in mag:
                mag[magazine[i]] = 1
            else:
                mag[magazine[i]] += 1
        # Iterates over ransomNote and for each letter it reduces the count of that letter in the hashmap by one
        # If a letter is present but the count in the hashmap is 0 then it returns False
        # If a letter isn't present it returns False
        # Else it returns True
        for i in range(len(ransomNote)):
            if ransomNote[i] not in mag:
                return False
            else:
                if mag[ransomNote[i]] <= 0:
                    return False
                else:
                    mag[ransomNote[i]] -= 1
        return True
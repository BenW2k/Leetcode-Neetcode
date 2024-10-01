class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag = {}
        for i in range(len(magazine)):
            if magazine[i] not in mag:
                mag[magazine[i]] = 1
            else:
                mag[magazine[i]] += 1
        for i in range(len(ransomNote)):
            if ransomNote[i] not in mag:
                return False
            else:
                if mag[ransomNote[i]] <= 0:
                    return False
                else:
                    mag[ransomNote[i]] -= 1
        return True
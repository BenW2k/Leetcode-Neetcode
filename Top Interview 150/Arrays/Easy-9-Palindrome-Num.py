class Solution:
    def isPalindrome(self, x: int) -> bool:
        r = 0
        n = x
        while n > 0:
            r *= 10
            r += n % 10
            n //= 10
        return r == x
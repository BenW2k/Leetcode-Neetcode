import re

def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        # Remove all non-alphanumeric characters.
        print(s)
        s = re.sub(r'[^a-zA-Z0-9]+', '', s).lower()
        print(s)


        # two-pointer technique to verify that the two pointers are the same character through the whole list.
        # Stops when i isn't less than or equal to j
        # If they're not the same at any point then return False, else True.
        
        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i] != s[j]:
                print(len(s))
                print(f'{i} + "and" + {j}')
                print('false')
                return False
            else:
                i += 1
                j -= 1
        
        print(f'{i} + "and" + {j}')
        print('True')
        return True

s = "A man, a plan, a canal: Panama"

isPalindrome(s)
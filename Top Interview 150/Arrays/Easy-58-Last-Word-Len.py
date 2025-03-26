class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # add words to list, return
        word_list = []
        word = ""

        for char in s:
            if char == " ":
                if len(word) >= 1:
                    word_list.append(word)
                    word = ""
            else:
                word += char
        
        if len(word) >= 1:
            word_list.append(word)
            
        return len(word_list[-1])
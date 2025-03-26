class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""

        length = len(str(num))

        for digit in str(num):
            digit = int(digit)
            if digit != 0:
                if length == 4:
                    res += ("M" * digit)
                elif length == 3:
                    if digit == 0:
                        continue
                    elif digit == 9:
                        res += "CM"
                    elif digit == 4:
                        res += "CD"
                    elif digit >= 5:
                        res+= ("D" + "C" * (digit % 5))
                    elif 0 < digit < 4:
                        res += ("C" * digit)
                elif length == 2:
                    if digit == 0:
                        continue
                    elif digit == 9:
                        res += "XC"
                    elif digit == 4:
                        res += "XL"
                    elif digit >= 5:
                        res += "L" + ("X" * (digit % 5))
                    elif 0 < digit < 4:
                        res += ("X" * digit)
                elif length == 1:
                    if digit == 0:
                        continue
                    elif digit == 9:
                        res += "IX"
                    elif digit == 4:
                        res += "IV"
                    elif digit >= 5:
                        res += "V" + ("I" * (digit % 5))
                    elif 0 < digit < 4:
                        res += ("I" * digit)
            length -= 1
        return res

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s != "":
            isTrue = False
            s_list = [x for x in s]
            t_list = [x for x in t]
            check_list = []

            j= 0
            for i in range(len(t_list)):
                    if t_list[i] == s_list[j]:
                        check_list.append(s_list[j])
                        if check_list == s_list:
                            isTrue = True
                            return isTrue
                        else:
                            j += 1
            return isTrue
        else:
            return True
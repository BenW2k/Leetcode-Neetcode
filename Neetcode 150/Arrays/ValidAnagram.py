def isAnagram(s, t):
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()
    if t_list == s_list:
        return True
    else:
        return False
isAnagram(s, t)
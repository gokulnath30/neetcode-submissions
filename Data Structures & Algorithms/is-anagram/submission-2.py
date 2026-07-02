class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        flag = False
        if s_len != len(t):
            return False
        for x in range(s_len):
            for y in range(t_len):
                if s[x] == t[y]:
                    flag = False
                    t = t[:y]+t[y+1:]   
                    t_len -= 1
                    break
                else:
                    flag = True
            if flag:
                return False
        return True
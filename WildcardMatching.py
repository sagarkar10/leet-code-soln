class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_l, p_l = len(s), len(p)
        save_s, save_p = None, None
        s_i = p_i = 0
        while s_i < s_l:

            if p_i < p_l and (p[p_i] == "?" or s[s_i] == p[p_i]):
                s_i += 1
                p_i += 1
            elif p_i < p_l and p[p_i] == "*":
                save_s, save_p = s_i, p_i
                p_i += 1
            elif save_p is not None:
                s_i, p_i = save_s + 1, save_p
            else:
                return False

        while p_i < p_l:
            if p[p_i] != "*":
                return False
            p_i += 1
        return True

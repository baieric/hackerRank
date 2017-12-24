# https://leetcode.com/problems/palindromic-substrings/description/

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        count = 0
        for i in range(l):
            x = 0
            while i - x >= 0 and i + x < l:
                if s[i-x] != s[i+x]:
                    break
                count += 1
                x += 1
        for i in range(l):
            x = 0
            while i - x >= 0 and i + 1 + x < l:
                if s[i-x] != s[i+1+x]:
                    break
                count += 1
                x += 1
        return count

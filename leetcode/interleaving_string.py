# Solution to https://leetcode.com/mockinterview/session/result/ew5pdfs/

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        cache = dict()

        def recurse(i1, i2, i3):
            if (i1, i2, i3) in cache:
                return cache[(i1, i2, i3)]
            if i1 == n1 and i2 == n2 and i3 == n3:
                cache[(i1, i2, i3)] = True
                return True

            if i1 == n1:
                cache[(i1, i2, i3)] = s3[i3:] == s2[i2:]
                return s3[i3:] == s2[i2:]

            if i2 == n2:
                cache[(i1, i2, i3)] = s3[i3:] == s1[i1:]
                return s3[i3:] == s1[i1:]

            if i3 == n3:
                cache[(i1, i2, i3)] = False
                return False

            if s1[i1] == s2[i2] and s1[i1] == s3[i3]:
                cache[(i1, i2, i3)] = recurse(i1+1, i2, i3 + 1) or recurse(i1, i2+1, i3+1)
                return recurse(i1+1, i2, i3 + 1) or recurse(i1, i2+1, i3+1)

            if s1[i1] == s3[i3]:
                cache[(i1, i2, i3)] = recurse(i1+1, i2, i3+1)
                return recurse(i1+1, i2, i3+1)

            if s2[i2] == s3[i3]:
                cache[(i1, i2, i3)] = recurse(i1, i2+1, i3+1)
                return recurse(i1, i2+1, i3+1)

            cache[(i1, i2, i3)] = False
            return False

        return recurse(0, 0, 0)

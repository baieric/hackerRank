# https://leetcode.com/problems/complex-number-multiplication/description/

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ap = a.index('+')
        a1 = int(a[:ap])
        a2 = int(a[ap+1:-1])

        bp = b.index('+')
        b1 = int(b[:bp])
        b2 = int(b[bp+1:-1])

        r1 = a1 * b1 - a2 * b2
        r2 = a1 * b2 + a2 * b1
        return str(r1) + "+" + str(r2) + "i"

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        d = dict()
        for i in A:
            for j in B:
                if i + j in d:
                    d[i+j] += 1
                else:
                    d[i+j] = 1

        count = 0
        for i in C:
            for j in D:
                if -(i+j) in d:
                    count += d[-(i+j)]
        return count

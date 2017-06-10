# https://leetcode.com/problems/kill-process

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        d = dict()
        for i in range(len(pid)):
            d[pid[i]] = []

        for i in range(len(ppid)):
            if ppid[i] != 0:
                d[ppid[i]].append(pid[i])

        ret = [kill]
        for i in ret:
            ret.extend(d[i])
        return ret

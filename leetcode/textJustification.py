# Solution to https://leetcode.com/problems/text-justification/
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ret = []
        index = 0
        lengths = [len(x) for x in words]
        while index < len(words):
            start = index
            end = index + 1
            lineLen = lengths[index]
            while end < len(words) and lineLen + 1 + lengths[end] <= maxWidth:
                lineLen += 1 + lengths[end]
                index += 1
                end = index + 1
            if end - start == 1:
                string = words[start]
                for i in range(maxWidth - lineLen):
                    string += " "
                ret.append(string)
            elif end == len(words):
                string = ""
                for i in range(start, end):
                    string += words[i]
                    if i != end - 1:
                        string += " "
                for i in range(maxWidth - lineLen):
                    string += " "
                ret.append(string)
            else:
                div = (maxWidth - lineLen) / (end - start - 1) # this many spaces per gap, at minimum
                rem = (maxWidth - lineLen) % (end - start - 1) # distribute remainder starting from left
                string = ""
                for i in range(start, end):
                    string += words[i]
                    if i == end - 1:
                        break
                    if rem > 0:
                        spaces = 2 + div
                        rem -= 1
                    else:
                        spaces = 1 + div
                    for j in range(spaces):
                        string += " "
                ret.append(string)
            index += 1
        return ret

# https://leetcode.com/problems/word-break/

from collections import defaultdict

class Solution(object):

    def wordBreak(self, s, wordDict):
        
        real_dict = defaultdict(list)
        for w in wordDict:
            real_dict[w[0:2]].append(w)

        matches = [False] * (len(s)+1)

        for i,c in enumerate(s):
            if i != 0 and matches[i] == 0:
                continue
    
            for w in real_dict[c] + real_dict[s[i:i+2]]:
                if w != s[i:i+len(w)]:
                    continue
                matches[i+len(w)] = True

            if matches[len(s)]:
                return True
    
        return False


class SolutionNaive(object):
    def findPath(self, i, matches):
        if i == len(matches):
            return True
        for m in matches[i]:
            if self.findPath(i+len(m), matches):
                return True
        return False

    def wordBreak(self, s, wordDict):
        
        real_dict = defaultdict(list)
        for w in wordDict:
            real_dict[w[0:2]].append(w)

        matches = []

        for i,c in enumerate(s):
            matches.append( set() )
            for w in real_dict[c] + real_dict[s[i:i+2]]:
                if s[i:i+len(w)] == w:
                    matches[i].add(w)
    
        return self.findPath(0, matches)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for l in s:
            if s.count(l) != t.count(l):
                return False
                
        return len(s) == len(t)
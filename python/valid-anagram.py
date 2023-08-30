class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for letter in s:
            if s.count(letter) != t.count(letter):
                return False
        return len(s) == len(t)
""" using count
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for l in ransomNote:
            if ransomNote.count(l) > magazine.count(l) or not magazine.count(l):
                return False

        return True
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for l in ransomNote:
            if l not in magazine:
                return False
            else:
                magazine = magazine.replace(l, "", 1)
        
        return True
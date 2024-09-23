class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for l in ransomNote:
            if ransomNote.count(l) > magazine.count(l) or not magazine.count(l):
                return False

        return True
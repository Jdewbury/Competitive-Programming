class Solution:
    def longestPalindrome(self, s: str) -> int:
        total = 0

        for l in set(s):
            num = s.count(l)
            if num % 2 == 0:
                total += num 
            elif num > 1:
                total += (num-1)

        return total + (len(s) != total)
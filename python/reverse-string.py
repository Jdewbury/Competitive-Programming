class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
        s[:] = s[::-1]
        """
        i = 0
        j = len(s) - 1
        while i < len(s) // 2:
            s[i], s[j - i] =  s[j - i], s[i]
            i += 1
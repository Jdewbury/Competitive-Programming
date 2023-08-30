class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        while n >= 1:
            if n == 1:
                return True
            n /= 2
        return False
        """
        if n <= 0:
            return False
        num = log10(n) / log10(2)
        return num == int(num)

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {} # use memoization

        def fib(n):
            # base cases
            if n == 1:
                return 1
            elif n == 2:
                return 2
            
            if n not in memo:
                memo[n] = fib(n-1) + fib(n-2)

            return memo[n]
        
        return fib(n)
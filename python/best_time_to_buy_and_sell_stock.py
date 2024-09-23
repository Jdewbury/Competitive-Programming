class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        min = float('inf')

        for num in prices:
            if num < min:
                min = num
            elif num - min > max:
                max = num - min
        return max
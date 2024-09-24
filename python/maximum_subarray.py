class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = float('-inf')
        curr_sum = 0

        for n in nums:
            curr_sum += n
            max_val = max(max_val, curr_sum)

            if curr_sum < 0:
                curr_sum = 0
            
        return max_val
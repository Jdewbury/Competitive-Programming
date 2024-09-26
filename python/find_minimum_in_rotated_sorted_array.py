class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0 
        j = len(nums) - 1
        min_val = float('inf')

        while i <= j:
            mid = (i + j) // 2
            val = nums[mid]

            min_val = min(min_val, val)

            if val < nums[j]:
                j = mid - 1
            else:
                i = mid + 1

        return min_val
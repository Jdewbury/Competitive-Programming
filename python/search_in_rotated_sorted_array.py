class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = (i + j) // 2
            val = nums[mid]

            if val == target:
                return mid
            
            if nums[i] <= val:
                if nums[i] <= target < val:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if val < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
            
        return -1
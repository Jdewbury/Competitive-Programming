class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 0
            
        for key, val in dict.items():
            if val >= len(nums) // 2:
                return key
        
        return 0
        """
        nums.sort()
        return nums[len(nums) // 2]
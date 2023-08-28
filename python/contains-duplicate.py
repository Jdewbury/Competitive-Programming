class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        using set()
        return len(nums) != len(set(nums))
        """
        dict = {}
        for i in nums:
            if i in dict:
                dict.pop(i)
            else:
                dict[i] = 0
        return len(dict) != len(nums)
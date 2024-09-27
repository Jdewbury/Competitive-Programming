class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subs = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    subs[i] = max(subs[i], subs[j] + 1)

        return max(subs)
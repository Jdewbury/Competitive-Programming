class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []

        for i in range(len(nums) - 2):
            # skip duplicate nums
            if i > 0 and nums[i] == nums[i-1]:
                continue 

            k = len(nums) - 1
            j = i + 1

            while j < k:
                tot = nums[i] + nums[j] + nums[k]
                if tot > 0:
                    k -= 1
                elif tot < 0:
                    j += 1
                else:
                    sol.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                    while j < k and nums[k] == nums[k-1]:
                        k -= 1

        return sol

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        j = 0
        
        while j < len(nums):
            bottom = nums[j]
            count = 0
            
            while j + 1 < len(nums) and nums[j+1] - nums[j] == 1:
                j += 1
                count += 1
            if count == 0:
                ranges.append([bottom])
            else:
                ranges.append([bottom, nums[j]])
            j+=1

        return [f"{num[0]}->{num[1]}" if len(num) == 2 else f"{num[0]}" for num in ranges]
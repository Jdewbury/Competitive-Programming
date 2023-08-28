class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        XOR approach 
        2^2 = 0
        2^2^3 = 3

        xor = 0
        for i in nums:
            xor ^= i
        return xor
        """
        dict = {}
        for i in nums:
            if i in dict:
                dict.pop(i)
            else:
                dict[i] = 0
        return sum(dict)
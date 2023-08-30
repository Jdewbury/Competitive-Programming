class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        pre = ""
        if len(strs) == 1:
            return strs[0]
        while i <= len(min(strs, key=len)):
            pre = strs[0][:i]
            for str in strs:
                if str[:i] != pre:
                    return strs[0][:i-1]
            i += 1

        return pre
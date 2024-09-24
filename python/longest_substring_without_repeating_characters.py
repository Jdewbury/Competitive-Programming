class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 1

        for i in range(len(s)):
            sub = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in sub:
                    sub += s[j]
                    max_len = max(max_len, len(sub))
                else:
                    max_len = max(max_len, len(sub))
                    break

        return max_len*(len(s) > 0)
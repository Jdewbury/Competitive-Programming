class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        rem = 0
        i = len(a) - 1
        j = len(b) - 1

        while j >= 0 or i >= 0 or rem:
            dig_a = int(a[i]) if i >=0 else 0
            dig_b = int(b[j]) if j >= 0 else 0
            
            total = dig_a + dig_b + rem

            rem = total // 2

            ans.append(str(total % 2))

            i -= 1
            j -= 1
        
        return ''.join(ans[::-1])
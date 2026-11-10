class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0

        for ch in s:
            sum = sum + ascii(ch)

        return sum
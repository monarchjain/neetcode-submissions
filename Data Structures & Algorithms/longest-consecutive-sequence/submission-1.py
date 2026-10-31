class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0
        length = 0
        for num in numbers:
            if num -1 not in numbers:
                current = num
                length = 1

                while current +1 in numbers:
                    current +=1
                    length +=1
            longest = max(longest,length)
        return longest
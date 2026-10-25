class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        max_freq = 0
        result = nums[0]
        for num in freq:
            if max_freq < freq[num]:
                max_freq = freq[num]
                result = num
        
        return result
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        for num in range(0,k):
            temp = nums[n-1]
            for i in range(n-2,-1,-1):
                nums[i+1] = nums[i]
            nums[0] = temp
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        if n == 0:
            return

        k = k % n

        for num in range(k):
            temp = nums[n - 1]

            for i in range(n - 2, -1, -1):
                nums[i + 1] = nums[i]

            nums[0] = temp
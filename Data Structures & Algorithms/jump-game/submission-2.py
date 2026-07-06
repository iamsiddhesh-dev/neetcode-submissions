class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last_index = n - 1

        for index in range(n-2, -1, -1):
            if nums[index] + index >= last_index:
                last_index = index
        
        return last_index == 0
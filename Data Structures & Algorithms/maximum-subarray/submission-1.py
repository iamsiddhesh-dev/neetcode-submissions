class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total = 0
        max_sum = float('-inf')

        for num in nums:

            total += num
            max_sum = max(total, max_sum)
            
            if total < 0:
                total = 0
            
        return max_sum
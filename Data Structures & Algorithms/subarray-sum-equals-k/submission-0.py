class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        current_sum = 0
        seen = {0:1}
        count = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            previous_sum = current_sum - k

            if previous_sum in seen:
                count += seen[previous_sum]
            
            seen[current_sum] = seen.get(current_sum, 0) + 1
        
        return count
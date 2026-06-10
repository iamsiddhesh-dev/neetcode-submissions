class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        longest = 0
        for idx,num in enumerate(nums):
            if num not in seen:
                seen[num] = idx
        for i in range(len(nums)):
            current_len = 1
            current = nums[i]
            while (current + 1) in seen:
                current_len += 1
                current += 1
            longest = max(current_len, longest)
        return longest
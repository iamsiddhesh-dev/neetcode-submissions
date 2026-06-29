class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        from collections import Counter

        count = Counter(nums)
        
        for num in nums:

            if count[num] == 1:
                return num
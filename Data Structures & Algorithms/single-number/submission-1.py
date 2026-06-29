class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for i in range(len(nums)):

            if count[nums[i]] == 1:
                return nums[i]
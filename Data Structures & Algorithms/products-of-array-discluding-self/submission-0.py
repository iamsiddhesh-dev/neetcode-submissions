class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        zero_count = nums.count(0)
        product_array = [0] * len(nums)
        
        for num in nums:
            if num != 0:
                product *= num

        for i in range(len(nums)):
            if zero_count >= 2:
                return product_array
            elif zero_count == 1:
                if nums[i] == 0:
                    product_array[i] = product
            else:
                product_array[i] = product // nums[i]
        
        return product_array
            
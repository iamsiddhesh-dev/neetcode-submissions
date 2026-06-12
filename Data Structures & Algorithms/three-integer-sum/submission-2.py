class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = set()
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and i != j and j != k and i != k:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(triplet)
        
        return list(result)
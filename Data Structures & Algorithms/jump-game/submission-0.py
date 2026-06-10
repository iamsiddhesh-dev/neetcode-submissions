class Solution:
    def canJump(self, nums: List[int]) -> bool:

        power = 0

        for value in nums:
            if power < 0:
                return False
            elif value > power:
                power += value
            power -= 1

        return True
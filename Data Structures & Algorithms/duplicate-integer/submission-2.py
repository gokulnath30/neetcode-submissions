class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checks = {}
        for i in nums:
            if i not in checks:
                checks[i] = 1
            else:
                return True
        return False 



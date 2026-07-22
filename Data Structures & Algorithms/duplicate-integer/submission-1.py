class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1. Creating Hash set of values:-
        seen_values = set(nums)
        
        # 2. Comparing lengths of hashsets with length of input list/array
        if len(nums) == len(seen_values):
            return False
        else: 
            return True
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1. Creating Hash set of seen values:-
        seen_values = set()
        
        for i in range(len(nums)):
            if nums[i] not in seen_values:
                seen_values.add(nums[i])
            else:
                return True 
        return False
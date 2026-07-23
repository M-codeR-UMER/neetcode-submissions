class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if list(s) == list(t):
        #     return True
        # for i in range(len(s)):
        #     for j in range(len(t)//2):
        #         if s[i] == t[j] 
        if sorted(s) == sorted(t):
            return True
        else:
            return False
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)
        
        ans = [0] * n * 2

        for index, value in enumerate(nums):
            ans[index] = value
            ans[index + n] = value
        
        return ans
        
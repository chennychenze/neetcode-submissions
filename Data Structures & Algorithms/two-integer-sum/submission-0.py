class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsMap = {} # key is num, val is index

        for i in range(len(nums)):
            cur = nums[i]
            if (target - cur) in numsMap:
                return [numsMap[target-cur], i]
            numsMap[nums[i]] = i

        


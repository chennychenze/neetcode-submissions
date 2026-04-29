class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsMap = {} # val -> index

        for i in range(len(nums)):
            cur = nums[i]
            if (target - cur) in numsMap:
                return [numsMap[target-cur], i]
            numsMap[nums[i]] = i


        # time: O(n)
        # space: O(n)

        


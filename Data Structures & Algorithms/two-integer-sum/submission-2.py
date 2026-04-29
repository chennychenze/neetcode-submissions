class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        myMap = {}  # key: element, value: index

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in myMap:
                return [myMap.get(diff), i]
                
            myMap[nums[i]] = i

        




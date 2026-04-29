class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        candidate = 0
        vote = 0

        for num in nums:
            # change to different candidate
            if vote == 0:
                candidate = num
            
            if num == candidate:
                vote += 1
            else:
                vote -= 1

        count = 0

        for num in nums:
            if num == candidate:
                count += 1

        if count > len(nums)//2:
            return candidate
        else:
            return 0
     
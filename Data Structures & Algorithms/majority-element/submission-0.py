class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        for key in count.keys():
            if count[key] > len(nums)/2:
                return key
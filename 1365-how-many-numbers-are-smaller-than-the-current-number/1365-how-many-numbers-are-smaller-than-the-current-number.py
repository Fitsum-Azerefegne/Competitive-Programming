class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
       output = []
       for i in range(len(nums)):
        num = 0
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                num += 1
        output.append(num)
       return output

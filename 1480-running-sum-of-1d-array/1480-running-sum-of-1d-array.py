class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        running_sum.append(nums[0])
        for i in range(1,len(nums)):
            running_sum.append(running_sum[i-1] + nums[i])
        return running_sum
     
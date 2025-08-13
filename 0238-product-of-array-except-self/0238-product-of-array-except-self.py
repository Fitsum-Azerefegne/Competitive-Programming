class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        # so we have left product for first element it is 1 
        # when we loop we always multiply the curr element with left_prod 
        # we use it for next j
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]
        # right one last element has no more right element so is 1
        # going from back we multipy it to the left_prod that is in output arr
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output
        
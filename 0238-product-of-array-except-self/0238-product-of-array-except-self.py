class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * (len(nums))
        for i in range(1, len(nums)):
            # left from i the product values
            products[i] = products[i - 1] * nums[i-1]
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= right_product
            right_product *= nums[i]
        return products

        
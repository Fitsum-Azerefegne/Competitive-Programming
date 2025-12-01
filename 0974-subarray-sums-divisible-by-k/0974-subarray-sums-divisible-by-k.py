class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        subarrays = 0
        curr_sum = 0
        remCount= {0:1}
        for num in nums:
            curr_sum += num
            rem = curr_sum % k
            if rem < 0:
                rem += k
            subarrays += remCount.get(rem,0)
            remCount[rem] = remCount.get(rem, 0) + 1
        return subarrays
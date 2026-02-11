class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_hash = defaultdict(int)
        n = len(nums)
        answer = []
        for num in nums:
            freq_hash[num] += 1
        for num, freq in freq_hash.items():
            if freq > n//3:
                answer.append(num)
        return answer

        
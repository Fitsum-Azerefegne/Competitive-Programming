class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1

        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        for num,freq in frequency.items():
            buckets[freq].append(num)

        result = []
        for freq in range(n, 0, -1):  
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:  
                    return result

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for n in nums1:
            if (n in nums2) and  (n not in intersection):
                intersection.append(n)
        return intersection
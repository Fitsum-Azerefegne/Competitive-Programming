class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for num1 in nums1:
            if (num1 in nums2) and (num1 not in intersection):
                intersection.append(num1)      
        return intersection
            

            

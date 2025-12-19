class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dd = defaultdict(int)
        for n in nums:
            dd[n] += 1
        major_count = 0
        major_element = 0
        for key in dd.keys():   
            if major_count < dd[key]:
                major_element = key
            major_count = max(major_count,dd[key])
        return major_element
            

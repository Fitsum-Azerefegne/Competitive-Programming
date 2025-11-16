class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        end = len(nums) - 1
        start = 0
        while start <= end:
            if nums[start] == val and nums[end] != val:
                nums[start] = nums[end]
                nums.pop()
                k += 1
                start += 1
                end -=1
            elif nums[start] != val :
                start +=1
            else:
                nums.pop()
                end -= 1
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return[]
    
class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        for i, num in enumerate(nums):
            comp = target - num

            if comp in hash:
                return [hash[comp], i]
        
            hash[num] = i
        
        return[]
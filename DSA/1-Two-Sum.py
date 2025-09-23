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
    
# class Solution(object):
#     def twoSum(self, nums, target):
#         hash = {}
#         for i, num in enumerate(nums):
#             comp = target - num

#             if comp in hash:
#                 return [hash[comp], i]
        
#             hash[num] = i
        
#         return[]

def find_pair(nums, target):
    seen = set()
    
    for num in nums:
        complement = target - num
        
        if complement in seen:
            return [num, complement]

        seen.add(num)

    return None


print(find_pair([10, 15, 3, 7], 17))
print(find_pair([1, 2, 3, 4], 8))
print(find_pair([5, 1, 6, 2, 4], 10))
print(find_pair([2, 8, 12, 7], 20))

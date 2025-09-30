class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(numbers)-1):
        #     for j in range(1+i, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return i+1,j+1

        start = 0
        end = len(numbers)-1

        while start < end:
            if numbers[start]+numbers[end] > target:
                end -= 1

            elif numbers[start]+numbers[end] < target:
                start +=1

            else:
                return [start+1, end+1]
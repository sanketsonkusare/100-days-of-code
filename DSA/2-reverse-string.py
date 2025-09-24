class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        """approach 1"""
        # a = s[:]
        # length = len(s)
        # for i in range(length):
        #     s[i] = a[length-1-i]

        """approach 2"""
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

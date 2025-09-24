class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        a = s[:]
        length = len(s)
        for i in range(length):
            s[i] = a[length-1-i]
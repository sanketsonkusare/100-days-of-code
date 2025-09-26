class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s = [c.lower() for c in s if c.isalnum()]
        # return all (s[i] == s[~i] for i in range(len(s)//2))
    
    # two pointer approach
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum(): i += 1
            while i < j and not s[j].isalnum(): j -= 1

            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1

        return True
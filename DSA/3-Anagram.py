class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # if sorted_s == sorted_t:
        #     return True
        # else:
        #     return False


        # return sorted(s) == sorted(t)


        # more efficient solution coz it checks for all the false case first that is much faster then it searches wather there exists another false case or not if not then it returns true
        
        if len(s)!=len(t):
            return False
        for index in set(s):
            if s.count(index)!=t.count(index):
                return False
        return True
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = ''.join(char.lower() for char in s if char.isalnum()).strip()
        for index in range(len(string)//2):
            if string[index] != string[-(index+1)]: return False
        return True
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #convert x into an array of strings
        string = [i for i in str(x)]
        #revrse the string to compare to
        reverse = list(reversed(string))
        
        string = ''.join(string)
        reverse = ''.join(reverse)
        
        #check if string and reverse are equal
        if string == reverse:
            return True
        else:
            return False
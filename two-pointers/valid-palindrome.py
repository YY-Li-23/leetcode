class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if s == " ":
            return True
        filtered = [c.lower() for c in s if c.isalnum()]  #Keep only alphanumeric and lowercase them
        return filtered == filtered[::-1]                 #c.isalnum() → keeps only letters and numbers.
        
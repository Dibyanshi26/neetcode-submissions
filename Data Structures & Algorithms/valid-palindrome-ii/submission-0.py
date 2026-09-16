class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Helper function jo normal palindrome check karta hai
        
        def is_subpalindrome(l: int, r: int)->bool:
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        left=0
        right=len(s)-1

        while left<right:
            if s[left]!=s[right]:
                return is_subpalindrome(left+1,right) or is_subpalindrome(left, right-1)
            left+=1
            right-=1
        return True




class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                if s[i].isupper():
                    s1+=(s[i]).lower()
                else:s1+=s[i]
        #print(s1)
        #return s1==s1[::-1]
        end=len(s1)-1;begin=0
        def rev(s1,start,end):
            if start>=end:return True
            else:
                if s1[start]!=s1[end]:return False
                return rev(s1,start+1,end-1)
        return rev(s1,begin,end)    

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res=""
        if(strs==None):
            return res
        else:
            c=0
            a=min(strs, key=len)
            while(a!=""):
                for i in range(len(strs)):
                    if(a == strs[i][0:len(a)]):
                        c+=1
                if(c==len(strs)):
                    break
                else:
                    c=0
                    a=a[0:len(a)-1]
            return a



        
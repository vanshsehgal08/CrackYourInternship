class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n=columnNumber
        s=""
        while(n>0):
            s=chr(ord('A')+(n-1)%26)+s
            n=(n-1)//26
        return s

        
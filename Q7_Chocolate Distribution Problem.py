#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        A.sort()
        min_diff = float('inf')
        i=0
        while M<=N:
            min_diff = min(min_diff, A[M-1]-A[i])
            M=M+1
            i+=1
        return min_diff
            
            
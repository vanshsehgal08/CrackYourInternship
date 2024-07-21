#User function Template for python3

class Solution:
    def isPossible(self, a, b, n, k):
        a.sort()
        b.sort(reverse=True)
        
        # Check if for every i, a[i] + b[i] >= k
        for i in range(n):
            if a[i] + b[i] < k:
                return False
        
        return True

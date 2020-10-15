class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        num_steps = 0
        size = len(A)
    
        for i in range(0, size-1):
            x = A[i+1] - A[i]
            y = B[i+1] - B[i]
            num_steps = num_steps + max(abs(x),abs(y))
            
        return num_steps

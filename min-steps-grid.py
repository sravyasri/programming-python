# Input Format
# Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith point respectively.



# Output Format
# Return an Integer, i.e minimum number of steps.
# Can move one step each in 8 directions
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

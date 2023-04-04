'''
1. For each row, we construct a histogram where each entry represents the number of consecutive ones 
in the colum with the same index.

2. Using a stack-based algorithm, we find the largest rectangle in the histogram
and we calculate its area 

3. We retain the maximum area among all histograms
'''

class Question2:
    
    def __init__(self, matrix):
        
        self.matrix = matrix
        self.Nrow = len(matrix)
        self.Ncol = len(matrix[0])
        

    def maximalRectangleOnes(self):
        if self.Nrow == 0: 
            return 0   

        histogram = [0] * self.Ncol
        maxArea = 0
        for row in range(self.Nrow):
            # For each row we construct a histogram formed by consecutives ones in the same column 
            
            for col in range(self.Ncol):
                if self.matrix[row][col] == 1:
                    histogram[col] += 1
                else:
                    histogram[col] = 0
            
            # For each histogram, we calculate the area of the largest rectangle inside the histogram
            maxArea = max(maxArea, self.largest_rectangle_area(histogram))
        return maxArea

    def largest_rectangle_area(self, histogram): 
        '''
        histogram: 1D array representing histogram obtained at a given row. Each element of the
                    histogram represents the number of consecutive ones at that index
        
        return an integer representing the maximum area of the histogram
        '''
        n = len(histogram)
        stack = [-1]
        maxArea = 0
        for i in range(n):
            while stack[-1] != -1 and histogram[stack[-1]] >= histogram[i]:
                currentHeight = histogram[stack.pop()]
                currentWidth = i - stack[-1] - 1
                maxArea = max(maxArea, currentWidth * currentHeight)
            stack.append(i)
        while stack[-1] != -1:
            currentHeight = histogram[stack.pop()]
            currentWidth = n - stack[-1] - 1
            maxArea = max(maxArea, currentWidth * currentHeight)
        return maxArea
    

B = [[0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1, 0],
     [1, 1, 0, 0, 1, 1, 0],
     [1, 1, 1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 1, 0]]

Sol = Question2(B)
print(Sol.maximalRectangleOnes())
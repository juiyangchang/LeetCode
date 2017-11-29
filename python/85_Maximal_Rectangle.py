class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        ans = 0
        
        for row_idx, row in enumerate(matrix):
            if row_idx == 0:
                height = list(map(int, row)) + [0]
            else:
                height = [height[j] + 1 if row[j] == '1' else 0 for j in range(len(row))] + [0]
            
            # stack maps to a non-decreasing list of heights
            stack = [-1]
            for i, h in enumerate(height):
                while stack and h < height[stack[-1]]:
                    j = stack.pop()
                    new_area = height[j] * (i - 1 - stack[-1])
                    if ans < new_area:
                        ans = new_area
                stack.append(i)
        return ans
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tri = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if i - 1 >= 0 and j - 1 >= 0 and j < i:
                    row.append(tri[i - 1][j - 1] + tri[i - 1][j])
                else:
                    row.append(1)
            tri.append(row)
        return tri

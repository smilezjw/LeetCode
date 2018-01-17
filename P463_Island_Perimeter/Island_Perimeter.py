# coding=utf8

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        land, edges = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    land += 1
                    if i > 0:
                        edges += grid[i-1][j]
                    if i < len(grid) - 1:
                        edges += grid[i+1][j]
                    if j > 0:
                        edges += grid[i][j-1]
                    if j < len(grid[0]) - 1:
                        edges += grid[i][j+1]
        return land*4 - edges


if __name__ == '__main__':
    solution = Solution()
    grid0 = [[0, 1, 0, 0],
             [1, 1, 1, 0],
             [0, 1, 0, 0],
             [1, 1, 0, 0]]
    print(solution.islandPerimeter(grid0))

# coding=utf8

class Solution(object):
    def __init__(self):
        self.visited = set()
        self.grid = []


    def maxAreaOfIsland(self, grid):
        self.grid = grid
        res = 0
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                res = max(res, self.depthTraverse(r, c))
        return res


    def depthTraverse(self, r, c):
        if not (0 <= r < len(self.grid) and 0 <= c < len(self.grid[0])
                and (r, c) not in self.visited
                and self.grid[r][c]):
            return 0
        self.visited.add((r, c))
        return (1 +
                self.depthTraverse(r+1, c) +
                self.depthTraverse(r-1, c) +
                self.depthTraverse(r, c+1) +
                self.depthTraverse(r, c-1))


if __name__ == '__main__':
    sol = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(sol.maxAreaOfIsland(grid))

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        uh = set()
        x = 0
        y = 0
        uh.add((x, y))

        for char in path:
            if char == "N":
                y += 1
            elif char == "S":
                y -= 1
            elif char == "E":
                x += 1
            else:
                x -= 1
            if (x, y) in uh:
                return True
            uh.add((x, y))
        return False


sol = Solution()
path = "NESW"
print(f"path: {path}, yes: {sol.isPathCrossing(path)}")

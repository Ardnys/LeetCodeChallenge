from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        uh = set()
        for cities in paths:
            uh.add(cities[0])

        for cities in paths:
            if cities[1] not in uh:
                return cities[1]

sol = Solution()
paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
print(f"dest: {sol.destCity(paths)}")

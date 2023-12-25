from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0

        visited = set()
        stacc = []

        for start_node in range(len(isConnected)):
            if start_node in visited:
                continue

            stacc.append(start_node)
            local_visited = set()

            while stacc:
                current_node = stacc.pop()
                local_visited.add(current_node)

                # Assign to a variable for better readability
                adj = isConnected[current_node]

                for neighbor in range(len(adj)):
                    if adj[neighbor] == 1 and neighbor not in local_visited:
                        stacc.append(neighbor)

            visited.add(frozenset(local_visited))

        return len(visited)


sol = Solution()
graph = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(f"graph: {graph}, number of provinces: {sol.findCircleNum(graph)}")

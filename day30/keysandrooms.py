from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def visit(room, visited):
            visited.add(room)
            # print(f"visiting room {room}. we have rooms {rooms}")

            for key in rooms[room]:
                if key not in visited:
                    visit(key, visited)

        visit(0, visited)

        return len(visited) == len(rooms)


sol = Solution()
rooms = [[1, 3], [3, 0, 1], [2], [0]]
print(f"yes: {sol.canVisitAllRooms(rooms)}")

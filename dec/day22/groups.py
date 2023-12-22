from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        uh = []
        current_size = 0
        mp = {}
        for i in range(len(groupSizes)):
            current_size = groupSizes[i]
            if not mp.get(current_size):
                mp[current_size] = []
            current_buffer = mp[current_size]
            # print(f"current size: {current_size}")
            if not current_buffer:
                mp[current_size] = [i]
            elif len(current_buffer) < current_size:
                current_buffer.append(i)
                # print(f"buffer has place: {current_buffer}. append {i}")
            else:
                # print(f"buffer filled: {current_buffer}")
                uh.append(current_buffer)
                mp.pop(current_size)
                mp[current_size] = [i]
                # print(f"new buffer: {mp[current_size]}")
        # print(mp)
        for value in mp.values():
            if value not in uh:
                uh.append(value)

        return uh


sol = Solution()
groups = [3, 3, 3, 3, 3, 1, 3]
print(f"groups: {groups}, partition: {sol.groupThePeople(groups)}")

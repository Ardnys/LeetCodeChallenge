from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        # wat is that python????
        # also slow
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]


sol = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(f"{k}th largest of {nums}: {sol.findKthLargest(nums, k)}")

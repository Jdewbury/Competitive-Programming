class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        # initialize a min-heap
        heapq.heapify(heap) 

        for n in nums[k:]:
            # check if num greater than heap head 
            if n > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, n)

        return heap[0]
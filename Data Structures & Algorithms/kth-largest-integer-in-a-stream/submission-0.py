class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.minHeap = nums
        self.k = k

        # turn minHeap into heap
        heapq.heapify(self.minHeap)

        # we only care about m-max values.. so lets cut the list to only k values

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        # add a value to the heap 
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

            # return kth largest value, which is the at the beginning of min heap
        return self.minHeap[0]
        

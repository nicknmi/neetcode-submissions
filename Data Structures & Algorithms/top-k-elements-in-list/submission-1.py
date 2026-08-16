class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        
        frequency = defaultdict(int)

        for num in nums:
            frequency[num] += 1

        heap = []

        for num, frq in frequency.items():
            heapq.heappush(heap, (frq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [n[1] for n in heap]


        
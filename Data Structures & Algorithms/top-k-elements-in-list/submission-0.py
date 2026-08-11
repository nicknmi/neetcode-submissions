class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        # get frequency 
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)

        max_heap = [(-val, key) for key, val in frequency.items()]
        heapq.heapify(max_heap)

        returnList = [] 
        for _ in range(k):
            returnList.append(heapq.heappop(max_heap)[1])
        
        return returnList


        
        

        
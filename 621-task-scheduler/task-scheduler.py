from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-count for count in counts.values()]
        # store all frequesncies in heap as negative
        heapq.heapify(maxHeap)
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            # pop from heap
            if maxHeap:
                # add 1 to decrease frequency(since frequencies are negative)
                new_freq = 1 + heapq.heappop(maxHeap)
                # store in queue
                if new_freq != 0:
                    q.append([new_freq, time + n])
            
            # check if queue time has come
            if q and q[0][1] == time:
                # if yes, add element to heap
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
                
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, priority, task):
        """
        Push a new task onto the queue with a specified priority.
        Lower priority values are processed first.
        
        :param priority: The priority of the task (lower is higher priority).
        :param task: The task data to be added to the queue.
        """
        heapq.heappush(self._queue, (priority, self._index, task))
        self._index += 1

    def pop(self):
        """
        Pop the highest priority task from the queue.
        
        :return: The task with the highest priority.
        """
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        """
        Check if the priority queue is empty.
        
        :return: True if the queue is empty, False otherwise.
        """
        return len(self._queue) == 0

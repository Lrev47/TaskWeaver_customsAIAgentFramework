from .priority_queue import PriorityQueue
from threading import Thread
import time

class TaskManager:
    def __init__(self):
        self.task_queue = PriorityQueue()
        self.running = False

    def add_task(self, task, priority=1):
        """
        Add a task to the task queue with a specified priority.
        
        :param task: A callable representing the task.
        :param priority: The priority of the task (lower is higher priority).
        """
        self.task_queue.push(priority, task)
    
    def start(self):
        """
        Start the task manager, which will begin processing tasks in the queue.
        """
        self.running = True
        Thread(target=self._run).start()

    def stop(self):
        """
        Stop the task manager, halting task processing.
        """
        self.running = False

    def _run(self):
        """
        Internal method to process tasks in the queue.
        """
        while self.running:
            if not self.task_queue.is_empty():
                task = self.task_queue.pop()
                try:
                    task()
                except Exception as e:
                    print(f"Error executing task: {e}")
            else:
                time.sleep(1)  # Wait for a second before checking the queue again


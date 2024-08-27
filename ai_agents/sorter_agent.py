class SorterAgent:
    def __init__(self):
        # Initialize routing logic and list of available worker agents
        self.worker_agents = {
            "text_processing": TextProcessingAgent(),
            "image_processing": ImageProcessingAgent()
        }

    def route_tasks(self, task_list):
        """
        Route tasks to the appropriate Worker Agents.
        
        :param task_list: A list of tasks to route.
        :return: Dictionary of results from the Worker Agents.
        """
        results = {}
        for task in task_list:
            if "text" in task:
                results["text"] = self.worker_agents["text_processing"].process("Sample text data")
            elif "image" in task:
                results["image"] = self.worker_agents["image_processing"].process("path_to_image.jpg")
            else:
                results[task] = "No suitable agent found."
        return results

# Example usage:
# sorter = SorterAgent()
# results = sorter.route_tasks(["Analyze text data", "Process images"])

class ErrorHandlerAgent:
    def __init__(self):
        # Initialize error database (could be a simple dictionary or database connection)
        self.error_db = {}

    def handle_error(self, error_message):
        """
        Handle errors by checking the error database and returning a solution if available.
        
        :param error_message: The error message reported by a Worker Agent.
        :return: Solution or instructions for the user.
        """
        solution = self.error_db.get(error_message, "No known solution. Please investigate further.")
        return solution

    def log_error(self, error_message, solution):
        """
        Log a new error and its solution into the error database.
        
        :param error_message: The error message to log.
        :param solution: The corresponding solution.
        :return: None
        """
        self.error_db[error_message] = solution

# Example usage:
# error_handler = ErrorHandlerAgent()
# solution = error_handler.handle_error("File not found")
# error_handler.log_error("File not found", "Please check the file path.")

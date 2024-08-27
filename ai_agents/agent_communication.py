class AgentCommunication:
    def __init__(self):
        # Initialize communication channels (e.g., message queue or shared memory)
        self.message_queue = []

    def send_message(self, sender, receiver, message):
        """
        Send a message from one agent to another.
        
        :param sender: The agent sending the message.
        :param receiver: The agent receiving the message.
        :param message: The content of the message.
        :return: None
        """
        self.message_queue.append({"sender": sender, "receiver": receiver, "message": message})
    
    def receive_message(self, receiver):
        """
        Receive messages intended for a specific agent.
        
        :param receiver: The agent receiving messages.
        :return: A list of messages.
        """
        messages = [msg for msg in self.message_queue if msg['receiver'] == receiver]
        self.message_queue = [msg for msg in self.message_queue if msg['receiver'] != receiver]
        return messages

# Example usage:
# comms = AgentCommunication()
# comms.send_message("Deconstructor", "Sorter", "Task list")
# sorter_messages = comms.receive_message("Sorter")

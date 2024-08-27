# AgentHiveMind Framework: Agent Overview

## Introduction

The AgentHiveMind framework operates on the principle of "one agent, one tool." Each AI agent is specialized for a specific task and interacts with other agents to complete complex workflows. The goal is to break down large, complex processes into smaller, manageable tasks, where each agent excels at a particular function. This modular approach allows for efficiency, scalability, and error handling through specialization.

This document provides an in-depth overview of the different agents within the framework, their roles, and their interactions with one another.

---

## Core Agents

### 1. Deconstructor Agent

**Role:**
The Deconstructor Agent serves as the entry point for user interaction. It is responsible for understanding the user's goal, business idea, or problem and breaking it down into actionable steps.

**Process:**

- Interacts with the user through the API or a UI form to understand their requirements.
- Asks probing questions to gain context and fill in any missing information.
- Converts the user's input into a structured plan with clearly defined tasks.
- Passes the generated task list to the Sorter Agent for further processing.

**Example Use Case:**
A user provides a business problem they want to solve. The Deconstructor Agent translates this into a series of steps, such as "Analyze customer feedback," "Process images," and "Compile a report."

---

### 2. Sorter Agent

**Role:**
The Sorter Agent is the central coordinator responsible for routing tasks to the appropriate Worker Agents based on their specialization. It ensures that each task is handled by the correct agent.

**Process:**

- Receives a task list from the Deconstructor Agent.
- Maps tasks to the corresponding Worker Agents based on the task type.
- Monitors the status of each task and manages the flow of information.
- If a Worker Agent reports an issue, the Sorter Agent reroutes the task to the Resolver Agent for handling.

**Example Use Case:**
The Sorter Agent receives tasks such as "Analyze text data" and "Process image." It sends the text task to the Text Processing Agent and the image task to the Image Processing Agent.

---

### 3. Worker Agents

**Role:**
Worker Agents are specialized in performing individual tasks. Each Worker Agent is equipped with a specific tool or function (e.g., text processing, image processing).

**Process:**

- Receives a task from the Sorter Agent that matches its specialization.
- Processes the task using its specific tool (e.g., NLP for text, image manipulation for images).
- Returns the processed data to the Sorter Agent or, in the case of an error, sends a message back explaining the issue.

**Types of Worker Agents:**

- **Text Processing Agent:** Specializes in analyzing and processing text data (e.g., tokenization, sentiment analysis).
- **Image Processing Agent:** Specializes in handling and processing image data (e.g., resizing, filtering).

**Example Use Case:**
The Text Processing Agent receives a task to analyze customer feedback. It performs sentiment analysis and returns the results to the Sorter Agent.

---

### 4. Resolver Agent (Error Handler Agent)

**Role:**
The Resolver Agent is responsible for handling errors or unprocessed tasks. It checks reported issues against a database of known solutions and either resolves the issue or informs the user.

**Process:**

- Receives error reports from the Sorter Agent when a Worker Agent fails to process a task.
- Looks up the error in a database of known issues and attempts to fix it.
- If a solution is found, it corrects the issue and notifies the Sorter Agent to retry the task.
- If no solution exists, it notifies the user with a detailed explanation and possible steps to resolve the problem.
- Logs the solution in the database for future use.

**Example Use Case:**
An image file is corrupted and cannot be processed by the Image Processing Agent. The Resolver Agent checks its database and suggests re-uploading the file in a different format.

---

### 5. Compiler Agent

**Role:**
The Compiler Agent is responsible for taking all processed data from the Worker Agents and organizing it into a final output document. This document should be well-structured, easy to read, and include references to any external resources or documentation.

**Process:**

- Receives processed data from the Sorter Agent once all tasks have been completed.
- Formats the data into a structured document, such as markdown, ensuring readability and including links to resources where applicable.
- Returns the final compiled document to the user via the API.

**Example Use Case:**
After all text and image data has been processed, the Compiler Agent creates a report summarizing the findings and attaches relevant images, ready to be shared with stakeholders.

---

### 6. Agent Communication

**Role:**
The Agent Communication module manages the messaging between agents, allowing them to send and receive data or status updates from one another. It acts as a communication layer within the framework.

**Process:**

- Handles message-passing between agents using a shared memory structure, a message queue, or another communication protocol.
- Ensures that all agents are aware of the task statuses and can react accordingly.

**Example Use Case:**
The Deconstructor Agent sends a task list to the Sorter Agent using the Agent Communication module, and the Sorter Agent sends a status update back once tasks are completed.

---

### 7. Local LLM Handler

**Role:**
The Local LLM Handler is responsible for integrating and managing local Language Models (LLMs). This allows the system to perform advanced language-related tasks using models hosted locally rather than relying on external APIs.

**Process:**

- Loads and manages a local LLM (e.g., GPT or a similar model).
- Receives requests from Worker Agents or other components and generates text-based responses or insights based on the input.
- Returns the generated output to the requesting agent.

**Example Use Case:**
The Text Processing Agent might call the Local LLM Handler to generate a summary or a natural language response based on the processed text data.

---

## Overall Workflow Example

1. **User Interaction:**

   - The user provides input through the API, such as describing a business problem.
   - The input is passed to the Deconstructor Agent.

2. **Task Breakdown:**

   - The Deconstructor Agent breaks down the user's input into actionable steps and creates a task list.
   - The task list is passed to the Sorter Agent.

3. **Data Processing:**

   - The Sorter Agent routes tasks to the appropriate Worker Agents (e.g., Text Processing Agent, Image Processing Agent).
   - Each Worker Agent processes its task and returns the results to the Sorter Agent.
   - If a Worker Agent encounters an error, the Sorter Agent reroutes the task to the Resolver Agent for resolution.

4. **Compilation:**

   - Once all tasks are completed, the Sorter Agent sends the processed data to the Compiler Agent.
   - The Compiler Agent compiles the data into a structured document (e.g., a report in markdown format).

5. **Final Output:**
   - The final document is sent back to the user through the API, completing the workflow.

---

## Conclusion

The AgentHiveMind framework is designed to be modular, scalable, and efficient by breaking down complex workflows into smaller, manageable tasks. Each agent plays a specialized role in the overall process, and by working together, they achieve the desired output with minimal user intervention.

This document provides an overview of the core agents and their interactions. For more specific implementation details, please refer to the individual agent files and additional documentation.

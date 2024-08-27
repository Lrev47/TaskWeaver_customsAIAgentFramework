# AgentHiveMind Architecture Overview

## Introduction

The **AgentHiveMind** framework is designed to be a modular, scalable, and efficient system where multiple specialized AI agents work together to solve complex problems. The architecture is built around the principle of "one agent, one tool," meaning that each agent is responsible for a specific task. These agents communicate and collaborate to complete larger workflows efficiently.

This document provides a detailed overview of the system architecture, including components, data flow, and key design principles.

---

## High-Level Overview

### Core Components:

1. **AI Agents**:

   - **Deconstructor Agent**: Interacts with the user, breaks down complex inputs into actionable tasks.
   - **Sorter Agent**: Manages the distribution of tasks to specialized Worker Agents.
   - **Worker Agents**: Execute specific tasks (e.g., text processing, image processing).
   - **Resolver Agent (Error Handler)**: Manages errors and issues, referencing a database of known solutions.
   - **Compiler Agent**: Compiles the final output from the processed data.
   - **Agent Communication**: Manages communication between agents, ensuring efficient data flow.
   - **Local LLM Handler**: Integrates and manages locally hosted Language Models (LLMs) for advanced language processing tasks.

2. **API**:

   - Built using FastAPI to manage user interactions and expose endpoints for triggering agent workflows.
   - WebSocket support for real-time communication and updates between the frontend and backend.

3. **Frontend**:

   - Developed with React.js, providing the user interface for interaction with the system, viewing task progress, error logs, and final outputs.

4. **Database**:

   - PostgreSQL database managed using Prisma ORM.
   - Stores user data, processed results, error logs, and other essential information.

5. **Task Management & Optimization**:

   - Implemented using Celery or RabbitMQ to handle task distribution and execution.
   - Includes a priority queue for optimizing task handling based on urgency or importance.

6. **Error Handling**:

   - Centralized error management through the Resolver Agent.
   - Logs errors and their resolutions in the database, enabling future agents to handle similar issues more effectively.

7. **Containerization**:
   - Docker and Docker Compose are used to containerize the application, ensuring consistent development and production environments.

---

## Data Flow

### Step-by-Step Workflow:

1. **User Input**:

   - The user interacts with the system through the frontend, providing their goal, business idea, or problem via a form.
   - The frontend sends this input to the backend API (managed by FastAPI).

2. **Task Deconstruction**:

   - The API triggers the **Deconstructor Agent**, which analyzes the user input.
   - The Deconstructor Agent breaks down the input into a list of actionable tasks and sends this list to the **Sorter Agent**.

3. **Task Distribution**:

   - The **Sorter Agent** receives the task list and determines which **Worker Agents** are best suited to handle each task.
   - Tasks are routed to the corresponding Worker Agents (e.g., text processing, image processing).
   - If a Worker Agent encounters an issue, the Sorter Agent reroutes the task to the **Resolver Agent**.

4. **Error Handling**:

   - The **Resolver Agent** attempts to resolve any errors by referencing a database of known issues and solutions.
   - If the Resolver Agent successfully fixes the issue, it notifies the Sorter Agent, which resubmits the task to the appropriate Worker Agent.
   - If no solution is available, the Resolver Agent logs the error and notifies the user via the frontend.

5. **Data Compilation**:

   - Once all tasks are completed, the **Sorter Agent** sends the processed data to the **Compiler Agent**.
   - The Compiler Agent organizes the data into a final output, typically in markdown format, and returns the compiled document to the user through the API.

6. **User Notification**:
   - The frontend receives the final compiled output and displays it to the user.
   - Real-time updates on task progress are provided via WebSocket connections between the frontend and backend.

### Key Design Principles:

- **Separation of Concerns**: Each agent is specialized for a single task, ensuring a clear division of responsibilities and easier debugging.
- **Scalability**: The architecture supports adding new Worker Agents for additional task types, allowing the system to scale as needed.
- **Resilience**: Error handling is centralized through the Resolver Agent, with error logs stored in a database to improve future performance.
- **Real-Time Communication**: WebSockets enable real-time communication, ensuring users are kept up-to-date on the status of their tasks.

---

## Detailed Component Overview

### 1. AI Agents

The core agents work together to process user input, handle tasks, and produce final outputs. The modular nature of the system allows for easy extension by adding new agents to handle different tasks.

- **Deconstructor Agent**: Acts as the interface between the user and the system, transforming user input into tasks.
- **Sorter Agent**: Manages the flow of tasks, ensuring each task is routed to the correct Worker Agent.
- **Worker Agents**: Specialized agents that perform specific tasks such as text or image processing.
- **Resolver Agent**: Handles errors and issues that arise during task processing.
- **Compiler Agent**: Compiles processed data into a coherent final document.
- **Agent Communication**: Facilitates communication between agents, ensuring efficient task routing and data exchange.

### 2. API

The FastAPI-based backend handles incoming HTTP requests and WebSocket connections. It serves as the entry point for user input and coordinates the agents.

- **Endpoints**: The API exposes endpoints for user interaction, triggering agents, and retrieving final outputs.
- **WebSocket Integration**: Provides real-time communication between the frontend and backend, ensuring users are kept up-to-date on task progress.

### 3. Frontend

The frontend, built with React.js, provides the user interface. Users can input their goals, track task progress, view error logs, and retrieve final outputs.

- **Dashboard**: Displays task progress, error logs, and compiled results.
- **WebSocket Integration**: Enables real-time updates from the backend.

### 4. Database

PostgreSQL is used as the primary database, with Prisma ORM handling the schema and migrations.

- **Models**: Define tables for storing user data, task results, error logs, etc.
- **Migrations**: Handle schema updates and ensure the database is in sync with the codebase.
- **Seeds**: Populate the database with initial data for development and testing.

### 5. Task Management & Optimization

Task management is handled using Celery or RabbitMQ, with a priority queue system ensuring that critical tasks are handled first.

- **Task Distribution**: Ensures that tasks are distributed to Worker Agents efficiently.
- **Queue Management**: Manages the order of task execution, with priority given to time-sensitive tasks.

### 6. Error Handling

Error handling is centralized through the Resolver Agent, which logs all issues and attempts to resolve them by referencing a database of known errors and solutions.

- **Error Database**: Stores known errors and solutions to streamline future error handling.
- **Logging**: All errors are logged in the database, allowing for tracking and analysis of recurring issues.

### 7. Containerization

Docker and Docker Compose are used to containerize the application, ensuring consistency across development, testing, and production environments.

- **Dockerfile**: Defines the environment for the application, including all dependencies.
- **docker-compose.yml**: Manages the multi-container setup for the app, including the API, frontend, database, and task manager.

---

## Future Considerations

The architecture is designed to be extendable and adaptable. Here are some future considerations for further development:

- **Agent Expansion**: Add new Worker Agents to handle more specialized tasks.
- **Cloud Integration**: Consider integrating cloud-based services for heavy processing tasks or large-scale deployments.
- **Security Enhancements**: Implement role-based access control (RBAC) and encryption for sensitive data.
- **AI Improvements**: Improve the capabilities of Worker Agents by integrating more advanced AI models, such as fine-tuned LLMs for specific tasks.

---

## Conclusion

The AgentHiveMind framework provides a flexible and efficient way to break down complex workflows into manageable tasks, each handled by specialized agents. The architecture is designed for scalability, resilience, and modularity, ensuring that the system can grow and adapt as new requirements arise.

By following this architecture, you can maintain a clear separation of concerns, optimize task execution, and ensure that your AI-driven system is both powerful and user-friendly.

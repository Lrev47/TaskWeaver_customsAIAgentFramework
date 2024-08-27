
# AgentHiveMind Setup Instructions

## Introduction
This document provides step-by-step instructions for setting up the **AgentHiveMind** framework. These instructions cover environment setup, dependencies installation, database configuration, running the application, and deployment considerations. By following these instructions, you'll have a fully functional AgentHiveMind system up and running.

--

## Prerequisites

Before starting, ensure that you have the following installed on your system:

1. **Python 3.8+**
2. **Node.js and npm** (for the frontend)
3. **PostgreSQL**
4. **Docker and Docker Compose** (for containerization)
5. **Git** (for version control)
6. **Poetry** (for Python dependency management)

---

## Step 1: Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/yourusername/agent-hivemind.git
cd agent-hivemind
```

---

## Step 2: Set Up Python Environment

### 2.1 Install Poetry
If you haven't installed Poetry yet, you can install it using the following command:

```bash
pip install poetry
```

### 2.2 Install Python Dependencies
Navigate to the project root directory and install the required dependencies using Poetry:

```bash
poetry install
```

### 2.3 Activate the Virtual Environment
Activate the virtual environment created by Poetry:

```bash
poetry shell
```

---

## Step 3: Set Up the Database

### 3.1 Install PostgreSQL
Make sure PostgreSQL is installed and running on your system. If you don't have it installed, follow the installation instructions for your operating system.

### 3.2 Create the Database
Create a new PostgreSQL database:

```bash
psql -U postgres
CREATE DATABASE agent_hivemind_db;
```

### 3.3 Configure Database Connection
In the project root, create a `.env` file to store your environment variables, including the database connection string. Use the following format:

```bash
DATABASE_URL=postgresql://username:password@localhost/agent_hivemind_db
SECRET_KEY=your_secret_key
```

Replace `username`, `password`, and `your_secret_key` with your actual PostgreSQL credentials and a secret key for the application.

### 3.4 Run Database Migrations
Run the Prisma migrations to set up the database schema:

```bash
poetry run prisma migrate deploy
```

### 3.5 Seed the Database (Optional)
To populate the database with initial data, run the seeding script:

```bash
poetry run python database/seeds.py
```

---

## Step 4: Set Up the Frontend

### 4.1 Install Node.js Dependencies
Navigate to the `frontend` directory and install the necessary dependencies:

```bash
cd frontend
npm install
```

### 4.2 Start the Frontend Development Server
Run the frontend development server:

```bash
npm start
```

The frontend will be available at `http://localhost:3000`.

---

## Step 5: Run the Backend

### 5.1 Start the FastAPI Server
Return to the project root and start the FastAPI backend server:

```bash
poetry run uvicorn api.main:app --reload
```

The backend will be available at `http://localhost:8000`.

### 5.2 WebSocket Communication
The backend also supports WebSocket communication for real-time updates. Ensure that the frontend and backend are both running to use this feature.

---

## Step 6: Running the Application with Docker (Optional)

### 6.1 Build and Start Containers
If you prefer to run the application in a Dockerized environment, use Docker Compose to build and start the containers:

```bash
docker-compose up --build
```

This command will build the Docker images and start the containers, including the frontend, backend, and PostgreSQL database.

### 6.2 Stop Containers
To stop the containers, run:

```bash
docker-compose down
```

---

## Step 7: Testing

### 7.1 Run Unit Tests
To run the unit tests for your agents and API, use the following command:

```bash
poetry run pytest
```

Make sure all tests pass before deploying the application to production.

---

## Step 8: Deployment Considerations

When deploying the application to production, consider the following:

- **Database Security**: Ensure that your PostgreSQL instance is secure and properly configured for production.
- **Environment Variables**: Use environment variables to manage sensitive data (e.g., `DATABASE_URL`, `SECRET_KEY`).
- **SSL/TLS**: Set up SSL/TLS certificates to secure HTTP and WebSocket traffic.
- **Scaling**: Consider using a cloud-based task queue service (e.g., AWS SQS) to scale task management.
- **Logging and Monitoring**: Implement logging and monitoring tools to track the application's performance and errors.

---

## Conclusion

By following these instructions, you should now have the **AgentHiveMind** framework set up and running on your local machine. The modular architecture and containerization support make it easy to extend and deploy the application. For further development, refer to the `architecture.md` and `agent_overview.md` files.

If you encounter any issues during setup, please refer to the documentation or reach out for support.

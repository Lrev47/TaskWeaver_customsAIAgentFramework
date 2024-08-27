from fastapi import APIRouter
from .websocket_handler import WebSocketManager

api_router = APIRouter()

# Example route to trigger the Deconstructor Agent
@api_router.post("/deconstruct/")
def deconstruct(user_input: str):
    # Here, you would interact with the DeconstructorAgent
    deconstructor = DeconstructorAgent()
    tasks = deconstructor.generate_tasks(user_input)
    return {"tasks": tasks}

# Example route to retrieve the final compiled output
@api_router.get("/compile/")
def compile_results():
    # Here, you would trigger the CompilerAgent
    compiler = CompilerAgent()
    processed_data = {"Task1": "Processed text", "Task2": "Processed image"}
    result = compiler.compile_data(processed_data)
    return {"compiled_result": result}

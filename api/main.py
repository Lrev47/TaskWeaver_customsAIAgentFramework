from fastapi import FastAPI
from .routes import api_router
from .websocket_handler import websocket_router

app = FastAPI()

# Include the API routes
app.include_router(api_router)

# Include WebSocket routes
app.include_router(websocket_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AgentHiveMind API!"}

# Example of running the application (can be placed in a separate run script if needed)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

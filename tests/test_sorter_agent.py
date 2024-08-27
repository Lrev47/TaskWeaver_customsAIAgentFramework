import pytest
from ai_agents.sorter_agent import SorterAgent
from ai_agents.worker_agents.text_processing_agent import TextProcessingAgent
from ai_agents.worker_agents.image_processing_agent import ImageProcessingAgent

def test_route_tasks():
    sorter = SorterAgent()
    tasks = ["Analyze text data", "Process images"]
    
    results = sorter.route_tasks(tasks)
    
    assert "text" in results
    assert "image" in results
    assert results["text"] == "Processed text"
    assert results["image"] == "Processed image"

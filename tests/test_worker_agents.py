import pytest
from ai_agents.worker_agents.text_processing_agent import TextProcessingAgent
from ai_agents.worker_agents.image_processing_agent import ImageProcessingAgent

def test_text_processing_agent():
    agent = TextProcessingAgent()
    result = agent.process("Sample text data")
    
    assert result is not None
    assert isinstance(result, list)  # Assuming tokenization returns a list of tokens

def test_image_processing_agent():
    agent = ImageProcessingAgent()
    result = agent.process("path_to_image.jpg")
    
    assert result is not None
    # Additional checks can be made depending on what `process` returns (e.g., resized image)

import pytest
from ai_agents.deconstructor_agent import DeconstructorAgent

def test_generate_tasks():
    deconstructor = DeconstructorAgent()
    tasks = deconstructor.generate_tasks("I need an analysis of my data.")
    
    assert isinstance(tasks, list)
    assert len(tasks) > 0
    assert "Analyze text data" in tasks

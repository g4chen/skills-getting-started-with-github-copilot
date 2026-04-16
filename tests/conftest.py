import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities

INITIAL_ACTIVITIES = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"],
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"],
    },
    "Basketball Team": {
        "description": "Competitive basketball team with regular practice and games",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["alex@mergington.edu"],
    },
    "Tennis Club": {
        "description": "Learn tennis skills and participate in friendly matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:00 PM",
        "max_participants": 16,
        "participants": ["grace@mergington.edu", "tyler@mergington.edu"],
    },
    "Art Studio": {
        "description": "Explore painting, drawing, and various art mediums",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["maya@mergington.edu"],
    },
    "Drama Club": {
        "description": "Theater performances and acting workshops",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 25,
        "participants": ["liam@mergington.edu", "ava@mergington.edu"],
    },
    "Science Club": {
        "description": "Hands-on experiments and STEM exploration",
        "schedule": "Mondays and Fridays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["noah@mergington.edu"],
    },
    "Debate Team": {
        "description": "Competitive debate and public speaking skills",
        "schedule": "Tuesdays and Fridays, 4:00 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["isabella@mergington.edu", "james@mergington.edu"],
    },
}


@pytest.fixture(autouse=True)
def reset_activities():
    activity_snapshot = copy.deepcopy(INITIAL_ACTIVITIES)
    activities.clear()
    activities.update(activity_snapshot)
    yield
    activities.clear()
    activities.update(activity_snapshot)


@pytest.fixture
def client():
    return TestClient(app)

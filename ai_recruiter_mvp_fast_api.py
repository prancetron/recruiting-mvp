"""
AI Recruiter MVP - Full Application (FastAPI)

This multi-part file contains:
  - `main.py`: FastAPI backend (resume screening, outreach, ATS placeholder integrations)
  - `requirements.txt`: Python dependencies
  - `Dockerfile`: containerization for deployment
  - `tests/test_main.py`: pytest unit tests (basic coverage for parsing + OpenAI call mocking)
  - `frontend/` : a tiny React dashboard (single-file app) for manual review and sending outreach
  - `seed_demo.py`: script to populate sample candidates into the local database

Notes:
  - You must populate environment variables in a `.env` file before running.
  - Run `seed_demo.py` before starting the application to populate demo candidate data:
      ```bash
      python seed_demo.py
      ```
  - For production, add secure storage for secrets, RBAC, logging/observability, and proper CI.
"""

# ==================== seed_demo.py ====================
import json
import os

# This is a simple in-memory or file-based demo seed.
DEMO_FILE = os.path.join(os.path.dirname(__file__), 'demo_candidates.json')

sample_candidates = [
    {
        "id": "c1",
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com",
        "resume_text": "Experienced Python developer with 5 years at TechCorp. Expert in FastAPI, Django, and cloud deployments. Led a team of 4 engineers.",
    },
    {
        "id": "c2",
        "name": "Bob Smith",
        "email": "bob.smith@example.com",
        "resume_text": "Frontend engineer specializing in React, Tailwind CSS, and responsive UI design. Built scalable dashboards for e-commerce clients.",
    },
    {
        "id": "c3",
        "name": "Carol Lee",
        "email": "carol.lee@example.com",
        "resume_text": "DevOps engineer with experience in Docker, Kubernetes, CI/CD pipelines, and AWS infrastructure. Implemented monitoring and alerting solutions.",
    }
]

with open(DEMO_FILE, 'w') as f:
    json.dump(sample_candidates, f, indent=2)

print(f"Demo candidates seeded to {DEMO_FILE}")

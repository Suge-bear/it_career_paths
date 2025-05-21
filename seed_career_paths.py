# seed_career_paths.py

from app import app, db
from models import CareerPath

career_paths = [
    {
        "name": "Help Desk Technician",
        "description": "The starting point for many IT pros. Responsibilities include user support, troubleshooting, and ticket management."
    },
    {
        "name": "System Administrator",
        "description": "Manages servers, networks, and internal systems. Builds on help desk experience with scripting and automation."
    },
    {
        "name": "Network Engineer",
        "description": "Designs and manages network infrastructure, routing, switching, and firewalls."
    },
    {
        "name": "Cloud Engineer",
        "description": "Focuses on building and managing cloud-based infrastructure using platforms like AWS, Azure, or GCP."
    },
    {
        "name": "Cybersecurity Analyst",
        "description": "Protects systems from cyber threats, monitors for breaches, and enforces security policies."
    },
    {
        "name": "DevOps Engineer",
        "description": "Combines development and operations to automate and improve CI/CD workflows."
    },
    {
        "name": "Database Administrator",
        "description": "Manages and optimizes databases for performance, security, and availability."
    },
    {
        "name": "IT Project Manager",
        "description": "Plans and leads IT projects, coordinating teams and resources to meet business goals."
    }
]

with app.app_context():
    for path in career_paths:
        existing = CareerPath.query.filter_by(name=path["name"]).first()
        if not existing:
            db.session.add(CareerPath(name=path["name"], description=path["description"]))
    db.session.commit()
    print("✅ Career paths seeded successfully!")

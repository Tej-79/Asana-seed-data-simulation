# Asana-seed-data-simulation
Creating High-Quality Seed Data for Asana RL Environment

## Overview
This project generates a **realistic, fully synthetic Asana-like workspace** for a large B2B SaaS organization with **5,000–10,000 employees**.  
The dataset is intended to serve as **high-quality seed data** for research and evaluation of AI agents operating in enterprise project-management environments.

The simulation models core Asana entities and workflows, including users, teams, projects, tasks, subtasks, comments, custom fields, and tags.  
All data is generated programmatically using predefined rules and heuristics to reflect real-world Asana usage patterns.

---

## What This Project Does
- Creates an Asana-style relational schema in SQLite
- Generates realistic synthetic data at enterprise scale
- Preserves referential integrity and temporal consistency
- Produces a single runnable pipeline that outputs a ready-to-use database

This project focuses on **data realism and methodology**, not UI or machine learning models.

---

## Requirements
- Python 3.8+
- SQLite (included with Python)
- Python dependencies listed in `requirements.txt`

---

## Setup Instructions

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run the generator
From the project root directory:
python src/main.py

## Output/Results
Running the generator creates a SQLite database at:
output/asana_simulation.sqlite

**Note:**  
The SQLite database file is intentionally **not committed to the repository** due to GitHub file size limits.  
It can be generated locally by running:  python src/main.py

---

The database represents a realistic Asana workspace, including:
- Thousands of users
- Hundreds of teams and projects
- Tens of thousands of tasks and subtasks
- Associated comments, custom fields, and tags

Data Characteristics

- All data is fully synthetic
- No real user, company, or proprietary data is used
- Task assignment, completion, and due dates follow realistic distributions
- Not all entities are fully populated (e.g., some tasks are unassigned or have no due date), reflecting real enterprise behavior

## Re-running the Generator

To regenerate the dataset, delete the existing database file:
    output/asana_simulation.sqlite
    Then run:
    python src/main.py
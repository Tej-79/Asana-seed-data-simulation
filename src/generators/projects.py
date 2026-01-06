import uuid
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

PROJECT_TYPES = ["Engineering", "Marketing", "Operations"]


def generate_projects(conn, team_ids, min_projects_per_team=2, max_projects_per_team=5):
    
    #Generates projects for each team.
    
    cursor = conn.cursor()
    project_ids = []

    now = datetime.utcnow()

    for team_id in team_ids:
        num_projects = random.randint(min_projects_per_team, max_projects_per_team)

        for _ in range(num_projects):
            project_id = str(uuid.uuid4())
            project_type = random.choice(PROJECT_TYPES)

            name = (
                f"{fake.word().capitalize()} Sprint"
                if project_type == "Engineering"
                else f"{fake.word().capitalize()} Campaign"
                if project_type == "Marketing"
                else f"{fake.word().capitalize()} Ops Initiative"
            )

            start_date = now.date() - timedelta(days=random.randint(0, 180))
            duration_days = (
                random.randint(14, 28)
                if project_type == "Engineering"
                else random.randint(30, 90)
            )
            end_date = start_date + timedelta(days=duration_days)
            created_at = (
                datetime.combine(start_date, datetime.min.time()).isoformat()
            )

            cursor.execute(
                """
                INSERT INTO projects (
                    project_id, team_id, name, project_type,
                    start_date, end_date, created_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    project_id,
                    team_id,
                    name,
                    project_type,
                    start_date.isoformat(),
                    end_date.isoformat(),
                    created_at,
                ),
            )

            project_ids.append(project_id)

    conn.commit()
    return project_ids

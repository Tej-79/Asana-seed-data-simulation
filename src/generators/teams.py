import uuid
from datetime import datetime, timedelta
import random
from faker import Faker

fake = Faker()

DEPARTMENTS = ["Engineering", "Marketing", "Operations"]


def generate_teams(conn, org_ids, total_teams=300):
 
    #Generates teams for the organization.
  
    cursor = conn.cursor()
    team_ids = []

    org_id = org_ids[0]
    now = datetime.utcnow()

    for _ in range(total_teams):
        team_id = str(uuid.uuid4())
        department = random.choice(DEPARTMENTS)
        name = f"{fake.word().capitalize()} {department} Team"
        created_at = (now - timedelta(days=random.randint(0, 600))).isoformat()

        cursor.execute(
            """
            INSERT INTO teams (team_id, org_id, name, department, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (team_id, org_id, name, department, created_at),
        )

        team_ids.append(team_id)

    conn.commit()
    return team_ids

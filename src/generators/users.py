import uuid
from datetime import datetime, timedelta
import random
from faker import Faker

fake = Faker()


def generate_users(conn, org_ids, total_users=6000):
    #Generates users for the organization.
    cursor = conn.cursor()
    users = []

    org_id = org_ids[0]
    now = datetime.utcnow()

    for _ in range(total_users):
        user_id = str(uuid.uuid4())
        full_name = fake.name()
        email = (full_name.lower().replace(" ", ".")+ "."+ user_id[:8]+ "@example.com")
        role = "admin" if random.random() < 0.08 else "member"
        created_at = (now - timedelta(days=random.randint(0, 730))).isoformat()

        cursor.execute(
            """
            INSERT INTO users (user_id, org_id, full_name, email, role, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (user_id, org_id, full_name, email, role, created_at),
        )

        users.append(user_id)

    conn.commit()
    return users

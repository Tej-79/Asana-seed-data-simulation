import uuid
from datetime import datetime
from faker import Faker

fake = Faker()


def generate_organizations(conn):
    #Generates a single organization representing the company workspace.
    cursor = conn.cursor()

    org_id = str(uuid.uuid4())
    name = fake.company()
    domain = name.lower().replace(" ", "") + ".com"
    created_at = datetime.utcnow().isoformat()

    cursor.execute(
        """
        INSERT INTO organizations (org_id, name, domain, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (org_id, name, domain, created_at),
    )

    conn.commit()
    return [org_id]

import uuid

DEFAULT_TAGS = [
    "urgent",
    "blocked",
    "bug",
    "security",
    "tech-debt",
    "frontend",
    "backend",
    "api",
]


def generate_tags(conn, org_ids):
    
    #Generates organization-level tags.
    
    cursor = conn.cursor()
    tag_ids = []

    org_id = org_ids[0]

    for tag_name in DEFAULT_TAGS:
        tag_id = str(uuid.uuid4())

        cursor.execute(
            """
            INSERT INTO tags (tag_id, org_id, name)
            VALUES (?, ?, ?)
            """,
            (tag_id, org_id, tag_name),
        )

        tag_ids.append(tag_id)

    conn.commit()
    return tag_ids

import uuid

DEFAULT_SECTIONS = ["To Do", "In Progress", "Done"]


def generate_sections(conn, project_ids):
    
    #Generates standard sections for each project.
  
    cursor = conn.cursor()
    section_ids = []

    for project_id in project_ids:
        for position, name in enumerate(DEFAULT_SECTIONS, start=1):
            section_id = str(uuid.uuid4())

            cursor.execute(
                """
                INSERT INTO sections (section_id, project_id, name, position)
                VALUES (?, ?, ?, ?)
                """,
                (section_id, project_id, name, position),
            )

            section_ids.append(section_id)

    conn.commit()
    return section_ids

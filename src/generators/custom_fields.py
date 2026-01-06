import uuid
import random

FIELD_TEMPLATES = [
    ("Priority", "enum", ["Low", "Medium", "High"]),
    ("Story Points", "number", ["1", "2", "3", "5", "8"]),
    ("Effort", "number", ["1", "2", "4", "8"]),
]


def generate_custom_fields(conn, project_ids, task_ids=None):
  
    #Generates custom field definitions per project and assigns values to tasks.

    cursor = conn.cursor()
    field_ids = []

    for project_id in project_ids:
        # Each project gets 2–3 custom fields
        selected_fields = random.sample(FIELD_TEMPLATES, random.randint(2, 3))

        for field_name, field_type, possible_values in selected_fields:
            field_id = str(uuid.uuid4())

            cursor.execute(
                """
                INSERT INTO custom_field_definitions (
                    field_id, project_id, name, field_type
                )
                VALUES (?, ?, ?, ?)
                """,
                (field_id, project_id, field_name, field_type),
            )

            field_ids.append((field_id, possible_values))

    # Assign custom field values to a subset of tasks
    if task_ids:
        for task_id in task_ids:
            if random.random() < 0.6:  # not all tasks have custom fields
                for field_id, values in random.sample(
                    field_ids, random.randint(1, min(2, len(field_ids)))
                ):
                    value_id = str(uuid.uuid4())
                    value = random.choice(values)

                    cursor.execute(
                        """
                        INSERT INTO custom_field_values (
                            value_id, field_id, task_id, value
                        )
                        VALUES (?, ?, ?, ?)
                        """,
                        (value_id, field_id, task_id, value),
                    )

    conn.commit()
    return [fid for fid, _ in field_ids]

import random


def generate_task_tags(conn, task_ids):

    #Assigns tags to tasks.

    cursor = conn.cursor()

    # Fetch all tag IDs
    cursor.execute("SELECT tag_id FROM tags")
    tag_ids = [row[0] for row in cursor.fetchall()]

    for task_id in task_ids:
        if random.random() < 0.5:  # not all tasks are tagged
            selected_tags = random.sample(
                tag_ids, random.randint(1, min(3, len(tag_ids)))
            )

            for tag_id in selected_tags:
                cursor.execute(
                    """
                    INSERT INTO task_tags (task_id, tag_id)
                    VALUES (?, ?)
                    """,
                    (task_id, tag_id),
                )

    conn.commit()

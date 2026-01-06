import uuid
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()


def generate_tasks(conn, project_ids, section_ids, user_ids):

    #Generates tasks and subtasks for projects.
   
    cursor = conn.cursor()
    task_ids = []

    now = datetime.utcnow()

    for project_id in project_ids:
        # number of tasks per project
        num_tasks = random.randint(30, 80)

        # sections for this project
        project_sections = [
            sid for sid in section_ids
        ]

        parent_tasks = []

        for _ in range(num_tasks):
            task_id = str(uuid.uuid4())
            name = fake.sentence(nb_words=5)
            description = fake.text(max_nb_chars=200) if random.random() < 0.7 else None

            assignee_id = (
                random.choice(user_ids) if random.random() > 0.15 else None
            )

            created_at = now - timedelta(days=random.randint(0, 180))

            # due date
            if random.random() < 0.1:
                due_date = None
            else:
                due_date = created_at.date() + timedelta(days=random.randint(3, 45))

            # completion
            completed = random.random() < 0.7
            completed_at = (
                created_at + timedelta(days=random.randint(1, 14))
                if completed
                else None
            )
            status = "completed" if completed else "open"

            section_id = random.choice(project_sections)

            cursor.execute(
                """
                INSERT INTO tasks (
                    task_id, project_id, section_id, parent_task_id,
                    name, description, assignee_id, due_date,
                    status, created_at, completed_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    task_id,
                    project_id,
                    section_id,
                    None,
                    name,
                    description,
                    assignee_id,
                    due_date.isoformat() if due_date else None,
                    status,
                    created_at.isoformat(),
                    completed_at.isoformat() if completed_at else None,
                ),
            )

            task_ids.append(task_id)
            parent_tasks.append(task_id)

        # generate subtasks (20–30% of tasks)
        for parent_task_id in random.sample(
            parent_tasks, int(len(parent_tasks) * random.uniform(0.2, 0.3))
        ):
            for _ in range(random.randint(2, 5)):
                subtask_id = str(uuid.uuid4())
                name = fake.sentence(nb_words=4)
                created_at = now - timedelta(days=random.randint(0, 180))

                cursor.execute(
                    """
                    INSERT INTO tasks (
                        task_id, project_id, section_id, parent_task_id,
                        name, description, assignee_id, due_date,
                        status, created_at, completed_at
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        subtask_id,
                        project_id,
                        random.choice(project_sections),
                        parent_task_id,
                        name,
                        None,
                        random.choice(user_ids),
                        None,
                        "open",
                        created_at.isoformat(),
                        None,
                    ),
                )

                task_ids.append(subtask_id)

    conn.commit()
    return task_ids

import uuid
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()


def generate_comments(conn, task_ids, user_ids):

    #Generates comments for a subset of tasks.
 
    cursor = conn.cursor()
    now = datetime.utcnow()

    for task_id in task_ids:
        # Only some tasks have comments
        if random.random() < 0.4:
            num_comments = random.randint(1, 5)

            for _ in range(num_comments):
                comment_id = str(uuid.uuid4())
                author_id = random.choice(user_ids)
                content = fake.sentence(nb_words=random.randint(6, 15))
                created_at = (now - timedelta(days=random.randint(0, 90))).isoformat()

                cursor.execute(
                    """
                    INSERT INTO comments (
                        comment_id, task_id, author_id, content, created_at
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (comment_id, task_id, author_id, content, created_at),
                )

    conn.commit()

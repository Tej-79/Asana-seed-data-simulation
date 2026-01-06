import random
from datetime import datetime, timedelta


def generate_team_memberships(conn, user_ids, team_ids):
    
    #Assigns users to teams with realistic team sizes.
    
    cursor = conn.cursor()
    now = datetime.utcnow()

    # Track how many teams each user is already in
    user_team_count = {user_id: 0 for user_id in user_ids}

    for team_id in team_ids:
        # Realistic team size: 5–12 members
        team_size = random.randint(5, 12)

        eligible_users = [
            uid for uid, count in user_team_count.items() if count < 2
        ]

        selected_users = random.sample(
            eligible_users, min(team_size, len(eligible_users))
        )

        for user_id in selected_users:
            joined_at = (now - timedelta(days=random.randint(0, 500))).isoformat()

            cursor.execute(
                """
                INSERT INTO team_memberships (team_id, user_id, joined_at)
                VALUES (?, ?, ?)
                """,
                (team_id, user_id, joined_at),
            )

            user_team_count[user_id] += 1

    conn.commit()

from utils.db import get_db_connection, initialize_schema

from generators.organizations import generate_organizations
from generators.users import generate_users
from generators.teams import generate_teams
from generators.team_memberships import generate_team_memberships
from generators.projects import generate_projects
from generators.sections import generate_sections
from generators.tasks import generate_tasks
from generators.comments import generate_comments
from generators.custom_fields import generate_custom_fields
from generators.tags import generate_tags
from generators.task_tags import generate_task_tags


DB_PATH = "output/asana_simulation.sqlite"
SCHEMA_PATH = "schema.sql"


def main():
    conn = get_db_connection(DB_PATH)

    # Step 1: Create tables
    initialize_schema(conn, SCHEMA_PATH)

    # Step 2: Generate data
    org_ids = generate_organizations(conn)
    user_ids = generate_users(conn, org_ids)
    team_ids = generate_teams(conn, org_ids)
    generate_team_memberships(conn, user_ids, team_ids)
    project_ids = generate_projects(conn, team_ids)
    section_ids = generate_sections(conn, project_ids)
    task_ids = generate_tasks(conn, project_ids, section_ids, user_ids)
    generate_comments(conn, task_ids, user_ids)
    field_ids = generate_custom_fields(conn, project_ids, task_ids)
    tag_ids = generate_tags(conn, org_ids)
    generate_task_tags(conn, task_ids)


    conn.close()
    print("Asana simulation database generated successfully.")


if __name__ == "__main__":
    main()

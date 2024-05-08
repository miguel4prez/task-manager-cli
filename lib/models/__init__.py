import sqlite3

CONN = sqlite3.connect('task_manager.db')
CURSOR = CONN.cursor()

create_users_table_sql = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);
"""

create_tasks_table_sql = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        task_name TEXT,
        priority TEXT,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    """

# Execute the SQL command to create the table
CURSOR.execute(create_users_table_sql)
CURSOR.execute(create_tasks_table_sql)

# Commit the changes
CONN.commit()
